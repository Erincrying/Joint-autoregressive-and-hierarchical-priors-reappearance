import argparse
import struct
import sys
import time
import compressai
import torch
import torch.nn.functional as F

from pathlib import Path
from PIL import Image
from compressai.zoo import models
from torchvision.transforms import ToPILImage, ToTensor
# from checkerboard import Checkerboard
# from CheckerboardCheng2020Anchor import CheckerboardCheng2020Anchor
# from CheckerboardCheng2020Attention import CheckerboardCheng2020Attention

# from Checker3d import Checker3d
from compressai.models.google import JointAutoregressiveHierarchicalPriors
metric_ids = {
    "mse": 0,
    "msssim": 1,
}


def options():
    parser = argparse.ArgumentParser(description="Example training script.")
    parser.add_argument(
        "-m",
        "--model",
        default="changeCheck3x3",
        choices=models.keys(),
        help="Model architecture (default: %(default)s)",
    )
    parser.add_argument(
        "--cuda",
        default=True,
        action="store_true",
        help="Use cuda")
    parser.add_argument(
        "--checkpoint",
        default='/home/ll/code/Joint-autoregressive-and-hierarchical-priors-reappearance/train_model/joint_renew_FIR_01/checkpoint.pth.tar',
        type=str,
        help="Path to a checkpoint"
    )
    parser.add_argument(
        "--image",
        default='/home/ll/code/Joint-autoregressive-and-hierarchical-priors-reappearance/kodak_re/kodim01.png',
        type=str,
        help="Path to a input images"
    )
    parser.add_argument(
        "--output",
        default='/home/ll/code/Joint-autoregressive-and-hierarchical-priors-reappearance/kodak_re/kodim01.bin',
        type=str
    )
    parser.add_argument(
        "--input",
        default='/home/ll/code/Joint-autoregressive-and-hierarchical-priors-reappearance/kodak_re',
        type=str
    )
    parser.add_argument(
        "--mode",
        default="encode"
    )
    parser.add_argument(
        "--show",
        default=True,
        type=bool
    )
    # 增加N和M两个参数，需要与训练时的N和M保持一致
    parser.add_argument(
        "--N",
        default=192,
        type=int
    )
    parser.add_argument(
        "--M",
        default=192,
        # default=320,
        type=int
    )
    parser.add_argument(
        "--G",
        default=24,
        type=int
    )

    args = parser.parse_args()

    return args


def load_image(filepath: str) -> Image.Image:
    return Image.open(filepath).convert("RGB")


def img2torch(img: Image.Image) -> torch.Tensor:
    return ToTensor()(img).unsqueeze(0)


def pad(x, p=2 ** 6):
    h, w = x.size(2), x.size(3)
    H = (h + p - 1) // p * p
    W = (w + p - 1) // p * p
    padding_left = (W - w) // 2
    padding_right = W - w - padding_left
    padding_top = (H - h) // 2
    padding_bottom = H - h - padding_top
    return F.pad(
        x,
        (padding_left, padding_right, padding_top, padding_bottom),
        mode="constant",
        value=0,
    )


def write_uints(fd, values, fmt=">{:d}I"):
    fd.write(struct.pack(fmt.format(len(values)), *values))


def write_bytes(fd, values, fmt=">{:d}s"):
    if len(values) == 0:
        return
    fd.write(struct.pack(fmt.format(len(values)), values))


def filesize(filepath: str) -> int:
    if not Path(filepath).is_file():
        raise ValueError(f'Invalid file "{filepath}".')
    return Path(filepath).stat().st_size


def read_uints(fd, n, fmt=">{:d}I"):
    sz = struct.calcsize("I")
    return struct.unpack(fmt.format(n), fd.read(n * sz))


def read_uchars(fd, n, fmt=">{:d}B"):
    sz = struct.calcsize("B")
    return struct.unpack(fmt.format(n), fd.read(n * sz))


def read_bytes(fd, n, fmt=">{:d}s"):
    sz = struct.calcsize("s")
    return struct.unpack(fmt.format(n), fd.read(n * sz))[0]


def crop(x, size):
    H, W = x.size(2), x.size(3)
    h, w = size
    padding_left = (W - w) // 2
    padding_right = W - w - padding_left
    padding_top = (H - h) // 2
    padding_bottom = H - h - padding_top
    return F.pad(
        x,
        (-padding_left, -padding_right, -padding_top, -padding_bottom),
        mode="constant",
        value=0,
    )


def torch2img(x: torch.Tensor) -> Image.Image:
    return ToPILImage()(x.clamp_(0, 1).squeeze())


def show_image(img: Image.Image):
    from matplotlib import pyplot as plt

    fig, ax = plt.subplots()
    ax.axis("off")
    ax.title.set_text("Decoded image")
    ax.imshow(img)
    fig.tight_layout()
    plt.show()


def encode(model, image, output, device):
    model.update()
    enc_start = time.time()

    img = load_image(image)
    start = time.time()
    model.eval()
    load_time = time.time() - start

    x = img2torch(img)
    # 新增一行，将输入转换到cuda上运行
    x = x.to(device)
    h, w = x.size(2), x.size(3)
    p = 64  # maximum 6 strides of 2
    x = pad(x, p)
    with torch.no_grad():
        out = model.compress(x)

    shape = out["shape"]
    with Path(output).open("wb") as f:
        write_uints(f, (h, w))
        write_uints(f, (shape[0], shape[1], len(out["strings"])))
        for s in out["strings"]:
            write_uints(f, (len(s[0]),))
            write_bytes(f, s[0])
    enc_time = time.time() - enc_start
    size = filesize(output)
    bpp = float(size) * 8 / (img.size[0] * img.size[1])
    print(
        f"{bpp:.3f} bpp |"
        f" Encoded in {enc_time:.2f}s (model loading: {load_time:.2f}s)"
    )

def decode(input, model, show, output=None):
    model.update()
    dec_start = time.time()
    with Path(input).open("rb") as f:
        original_size = read_uints(f, 2)
        shape = read_uints(f, 2)
        strings = []
        n_strings = read_uints(f, 1)[0]
        for _ in range(n_strings):
            s = read_bytes(f, read_uints(f, 1)[0])
            strings.append([s])

    start = time.time()
    model.eval()
    load_time = time.time() - start

    with torch.no_grad():
        out = model.decompress(strings, shape)
    x_hat = crop(out["x_hat"], original_size)
    img = torch2img(x_hat)
    dec_time = time.time() - dec_start
    print(f"Decoded in {dec_time:.2f}s (model loading: {load_time:.2f}s)")

    if show:
        show_image(img)
    if output is not None:
        img.save(output)


if __name__ == "__main__":
    args = options()
    device = "cuda" if args.cuda and torch.cuda.is_available() else "cpu"

    # 增加两行获取待编码图像的尺寸
    x = img2torch(load_image(args.image))
    p = 64
    x = pad(x, p)
    h, w = x.size(2), x.size(3)
    # 选取模型时设置具体的参数，使得编解码时的mask尺寸与输入图像保持一致
    # model = Checker3d(N=args.N, M=args.M, G=args.G)
    model = JointAutoregressiveHierarchicalPriors(N=args.N, M=args.M)
    
    
    net = model.to(device)
    checkpoint = torch.load(args.checkpoint, map_location=device)
    net.load_state_dict(checkpoint["state_dict"])
    # if args.mode.equal("encode"):
    if args.mode == "encode":
        encode(net, args.image, args.output, device)
    else:
        decode(args.input, net, args.show, args.output)

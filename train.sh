conda activate PTGPUPY37
python3 train.py -m mbt2018 -d /home/ll/code/CompressAI_reappearance/imageNet --epochs 500 -lr 1e-4 --lambda 0.0016 --batch-size 16 --cuda --save> log.out


# conda activate torchll
python3 train.py -m mbt2018 -d /home/ll/datasets/imageNet1000t --epochs 2000 -lr 1e-4 --lambda 0.03 --batch-size 16 --cuda --save > log.out
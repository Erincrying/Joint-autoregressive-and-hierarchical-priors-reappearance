# conda activate torchll
python3 train.py -m mbt2018 -d /home/disk/lilin/datasets/zqbDatasets/Valimagenet --epochs 500 -lr 1e-4 --lambda 0.045 --batch-size 16 --cuda --save > log.out
#!/usr/bin/env bash
#SBATCH --gpus-per-node=V100:1
#SBATCH -t 0-2:00:00

#SBATCH --output=logs/train.out

module load GCC/8.3.0  CUDA/10.1.243  OpenMPI/3.1.4
module load PyTorch/1.6.0-Python-3.7.4
module load Python/3.7.4

source /cephyr/users/murathan/Alvis/deep/bin/activate

out_dir="xx"
rm -rf ${out_dir}
./scripts/train.sh ${out_dir}

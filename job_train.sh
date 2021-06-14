#!/usr/bin/env bash
#SBATCH --gpus-per-node=V100:1
#SBATCH -t 0-1:00:00

#SBATCH --output=logs/train-%j.out

module load GCC/8.3.0  CUDA/10.1.243  OpenMPI/3.1.4
module load PyTorch/1.6.0-Python-3.7.4
module load Python/3.7.4

source /cephyr/users/murathan/Alvis/deep/bin/activate

if [ $# -ne 2 ]
  then
    echo "Illegal number of parameters"
  else
  echo "Sentence count: ${1}   length: ${2}"
  ./scripts/train.sh "$1" "$2"
fi
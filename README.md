# <p align=center>Scene Segmentation through Sequential Sentence Classification</p>
This repo has code for our paper ["Breaking the Narrative: Scene Segmentation through Sequential Sentence Classification"](http://lsx-events.informatik.uni-wuerzburg.de/files/stss2021/proceedings/kurfali_wiren.pdf) that ranked 1st at the [Shared Task on Scene Segmentation (STSS)](http://lsx-events.informatik.uni-wuerzburg.de/stss-2021/).

### How to run
python utils/preprocess.py data_path output_path
./scripts train 25 50
### on slurm
srun -A SNIC2022-22-655 -t 1-00:00:00 --gpus-per-node=V100:1 ./scripts train 25 50
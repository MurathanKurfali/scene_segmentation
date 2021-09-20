# <p align=center>Scene Segmentation</p>
This repo has code for our paper ["Breaking the Narrative: Scene Segmentation through Sequential Sentence Classification"](http://lsx-events.informatik.uni-wuerzburg.de/files/stss2021/proceedings/kurfali_wiren.pdf).

### How to run

The easist way to run our model on your data is through Docker. 

./build.sh

./run.sh

(inside the container): source pip/bin/activate

(inside the container): python predict.py


### Citing

If you use the data or the model, please cite,
```
@inproceedings{kurfali2021breaking,
  title={Breaking the Narrative: Scene Segmentation through Sequential Sentence Classification},
  author={Kurfal{\i}, Murathan and Wir{\'e}n, Mats}
  journal={Shared Task on Scene Segmentation},
  year={2021}
}
```

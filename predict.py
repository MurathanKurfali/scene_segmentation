import glob
import os

import shutil
from src.utils.preprocess import read_json
from src.utils.postprocess import post_process, post_process2
import subprocess


def reset_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)


if __name__ == "__main__":
    test_folder = "data/test"
    temp_folder = "data/tmp"
    pred_folder = "predictions"
    pred_folder2 = "predictions2"

    listing = glob.glob('src/large*')

    for model_file in listing:
        model_file = "{}/model.tar.gz".format(model_file)
        print("**********", model_file)
        test_files = sorted(os.listdir("data/test"))
        reset_folder(temp_folder)
        reset_folder(pred_folder)
        reset_folder(pred_folder2)

        for test_file in test_files:
            if False and "9783845397535" not in test_file:
                continue
            test_file_path = "{}/{}".format(test_folder, test_file)
            tmp_file_path = "{}/{}".format(temp_folder, test_file + "l")
            predicted_file_path = "{}/{}".format(pred_folder, test_file + ".pred")

            read_json(test_file_path, temp_folder, use_filename_as_split=True)  ## saves to data/tmp/

            subprocess.run('src/scripts/predict.sh {} {} {}'.format(model_file, tmp_file_path, predicted_file_path),
                           shell=True)
            print("post-processing")
            post_process(test_file_path, tmp_file_path, predicted_file_path)
            post_process2(test_file_path, tmp_file_path, predicted_file_path, out_file="{}/{}".format(pred_folder2, test_file + ".json"))

            # os.remove(predicted_file_path)
            print("done" + "#" * 15)
    # shutil.rmtree(temp_folder)

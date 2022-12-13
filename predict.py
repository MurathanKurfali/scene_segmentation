import os

import shutil
from utils.preprocess import read_json
from utils.postprocess import post_process
import subprocess
import sys

def reset_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)


if __name__ == "__main__":
    test_folder = sys.argv[1]
    temp_folder = "data/tmp"
    pred_folder = sys.argv[2]
    model_file = sys.argv[3]

    reset_folder(temp_folder)
    reset_folder(pred_folder)

    for test_file in sorted(os.listdir(test_folder)):
        test_file_path = "{}/{}".format(test_folder, test_file)
        tmp_file_path = "{}/{}".format(temp_folder, test_file + "l")
        predicted_file_path = "{}/{}".format(pred_folder, test_file + ".pred")

        read_json(test_file_path, temp_folder, use_filename_as_split=True)  ## saves to data/tmp/

        subprocess.run('predict.sh {} {} {}'.format(model_file, tmp_file_path, predicted_file_path),
                       shell=True)
        print("post-processing")
        post_process(test_file_path, tmp_file_path, predicted_file_path)

        # os.remove(predicted_file_path)
        print("{} done".format(test_file))
    print("#" * 15)

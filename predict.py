import os

import shutil
from code.utils.preprocess import read_json
from code.utils.postprocess import post_process
import subprocess


def reset_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)


if __name__ == "__main__":
    test_folder = "data/test"
    temp_folder = "data/tmp"
    pred_folder = "predictions"
    model_file = "model/model.tar.gz"

    test_files = [os.path.join(test_folder, f) for f in sorted(os.listdir("data/test"))]
    reset_folder(temp_folder)
    for test_file_path in test_files:
        read_json(test_file_path, temp_folder, use_filename_as_split=True)

        subprocess.run('code/scripts/predict.sh {} {} {}'.format(model_file, test_file_path.replace("test", "tmp").replace("json", "jsonl"), test_file_path.replace("data/test", pred_folder)),
                       shell=True)
        predicted_file_tmp_dir = test_file_path.replace("data/test", pred_folder) + ".pred"
        print("post-processing")
        post_process(test_file_path, predicted_file_tmp_dir)
        os.remove(predicted_file_tmp_dir)
        print("done" + "#" * 15)
        break
    # shutil.rmtree(temp_folder)

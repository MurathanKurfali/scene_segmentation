import json
from collections import deque, defaultdict
import logging
from logging import info
from pathlib import Path
from pprint import pprint, pformat
from typing import Dict
import itertools
import json
import jsonlines
import sys

import numpy as np
from nltk import flatten
from sklearn.metrics import f1_score, classification_report, confusion_matrix

logging.getLogger().setLevel(logging.DEBUG)

def read_jsonlines(file_path):
    content = []
    with jsonlines.open(file_path) as f:
        for line in f.iter():
            content.append(line)
    return content

def eval_folder(gold_dir: Path, pred_dir: Path):
    results = []
    f1_scores = []

    for gold_file in gold_dir.iterdir():
        pred_file = pred_dir.joinpath(gold_file.name.replace("jsonl", "json.pred"))
        if not pred_file.is_file():
            print(
                "Missing annotations for file %s! Please write all predictions to the folder `/predictions` with the same "
                "name as the input file" % str(
                    gold_file))
            continue
        original_file = read_jsonlines(gold_file)
        pred = flatten([x["labels"] for x in read_jsonlines(pred_file)])
        pred = [p.replace("_label", "") for p in pred ]
        print(sorted(set(pred)))
        print(gold_file, f1_score(original_file[0]["labels"][:len(pred)], pred, average=None, labels=sorted(set(pred))))
        print(gold_file, f1_score(original_file[0]["labels"][:len(pred)], pred, average="weighted", labels=sorted(set(pred))))


    logging.info("Mean macro avg. f1 score over all files: %.2f" % np.mean(f1_scores))

if __name__ == '__main__':
    gold_dir = Path("data/tmp")
    pred_dir = Path("predictions")


    eval_folder(gold_dir=gold_dir, pred_dir=pred_dir)

    print()

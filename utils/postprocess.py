import itertools
import os
import json
import shutil
import string
from collections import Counter
import jsonlines


def read_jsonlines(file_path):
    content = []
    with jsonlines.open(file_path) as f:
        for line in f.iter():
            content.append(line)
    return content


if __name__ == "__main__":
    pred_file_path = "../data/predictions/pred.json"
    test_file_path = "../data/trial/test.jsonl"
    out_dir = "../data/predictions/final.json"
    pred, test = read_jsonlines(pred_file_path), read_jsonlines(test_file_path)
    labels = list(itertools.chain(*[line["labels"] for line in pred]))
    indicies = list(itertools.chain(*[line["indices"] for line in test]))
    grouped = []
    labels = list(zip(labels, indicies))
    group = {}
    for i, x in enumerate(labels):
        l = x[0].replace("_label", "")
        if i == 0:
            prev_l = l.replace("-B", "")
            group[prev_l] = [x[1]]
        else:
            if "-B" in l:
                grouped.append( {"begin": list(group.values())[0][0][0], "end": list(group.values())[-1][-1][-1], "type": list(group.keys())[0]})
                group = {l.replace("-B", ""): [x[1]]}
                prev_l = l.replace("-B", "")
            else:
                if l == prev_l:
                    group[prev_l].append(x[1])
                else:
                    grouped.append({"begin": list(group.values())[0][0][0], "end": list(group.values())[-1][-1][-1], "type": list(group.keys())[0]})
                    group = {l.replace("-B", ""): [x[1]]}
                    prev_l = l.replace("-B", "")

    print(grouped)
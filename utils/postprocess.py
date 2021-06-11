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
    pred_file_path = "../data/predictions/9783732522033.json"
    #pred_file_path = "../data/trial/test.jsonl"

    test_file_path = "../data/trial/test.jsonl"
    out_dir = "../data/output/9783732522033.json"
    original_file_path = "/home/murathan/Desktop/scene-segmentation/json/9783732522033.json"


    original_file = json.load(open(original_file_path))
    pred, test = read_jsonlines(pred_file_path), read_jsonlines(test_file_path)
    labels = list(itertools.chain(*[line["labels"] for line in pred]))
    indicies = [(line["begin"], line["end"]) for line in original_file["sentences"]]
    grouped = []
    labels = list(zip(labels, indicies))
    group = {}
    last_border= 0
    for i, x in enumerate(labels):
        if i > 2600:
            print()
        l = x[0].replace("_label", "")
        if i == 0:
            prev_l = l.replace("-B", "")
            group = [x[1]]
        else:
            if "-B" in l:
                initial_punc_count = len(original_file["text"][last_border:group[-1][-1]]) - len(original_file["text"][last_border:group[-1][-1]].lstrip(" "))
                e = len(original_file["text"][last_border:group[-1][-1]]) - len(original_file["text"][last_border:group[-1][-1]].rstrip("  "))

                grouped.append({"begin": last_border, "end": group[-1][-1]-e, "type": prev_l})
                group = [x[1]]
                last_border = grouped[-1]["end"]
                prev_l = l.replace("-B", "")
            else:
                if l == prev_l:
                    group.append(x[1])
                else:
                    e = len(original_file["text"][last_border:group[-1][-1]]) - len(original_file["text"][last_border:group[-1][-1]].rstrip("  "))
                    grouped.append({"begin": last_border, "end": group[-1][-1] - e, "type": prev_l})
                    group = [x[1]]
                    last_border = grouped[-1]["end"]
                    prev_l = l.replace("-B", "")

    print(grouped)
    output = {"text": original_file["text"], "scenes": grouped}

    json.dump(output, open(out_dir, "w"))

import itertools
import json
import jsonlines
import sys


def read_jsonlines(file_path):
    content = []
    with jsonlines.open(file_path) as f:
        for line in f.iter():
            content.append(line)
    return content


def post_process(original_file_path, tmp_file_path, pred_file_path, out_file=None):
    if not out_file:
        out_file = pred_file_path.replace(".pred", "")

    original_file = json.load(open(original_file_path, ))
    pred = read_jsonlines(pred_file_path)
    tmp_file_sent_boundaries = read_jsonlines(tmp_file_path)
    labels = list(itertools.chain(*[line["labels"] for line in pred]))
    labels = [l.replace("_label","") if "-"  in l else "x" for l in labels]
    indexes = [(line[0], line[1]) for line in tmp_file_sent_boundaries[0]["indices"]]
    labels = list(zip(labels, indexes))
    scenes = []
    for l in labels:
        if "x" not in l[0]:
            scenes.append({"begin": l[1][0], "end": -1, "type": l[0].replace("-B", "")})

    output = {"text": original_file["text"], "scenes": scenes}
    if out_file.endswith("l"):
        out_file = out_file[:-1]
    json.dump(output, open(out_file, "w"))


if __name__ == "__main__":
    no = "9783845397535"
    pred_file_path = "predictions2/{}.json.pred".format(no) # sys.argv[1]  # "data/predictions/{}.pred".format(test_file)
    original_file_path = "data/test/{}.json".format(no)   #sys.argv[2]
    tmp_file_path = "data/tmp/{}.jsonl".format(no)   #sys.argv[2]

    post_process(original_file_path, tmp_file_path,  pred_file_path, out_file="predictions2/{}.json".format(no))
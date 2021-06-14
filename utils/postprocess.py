import itertools
import json
import jsonlines
from preprocess import test_file


def read_jsonlines(file_path):
    content = []
    with jsonlines.open(file_path) as f:
        for line in f.iter():
            content.append(line)
    return content


if __name__ == "__main__":
    pred_file_path = "../data/predictions/{}".format(test_file)
    # pred_file_path = "../data/ss/test.jsonl"

    test_file_path = "../data/ss/test.jsonl"
    out_dir = "../data/output/{}".format(test_file)
    original_file_path = "/home/murathan/Desktop/scene-segmentation/json/{}".format(test_file)

    original_file = json.load(open(original_file_path))
    pred, test = read_jsonlines(pred_file_path), read_jsonlines(test_file_path)
    labels = list(itertools.chain(*[line["labels"] for line in pred]))
    indicies = [(line["begin"], line["end"]) for line in original_file["sentences"]]
    grouped = []
    labels = list(zip(labels, indicies))
    group = {}
    last_border = 0
    for i, x in enumerate(labels):
        l = x[0].replace("_label", "")
        if i == 0:
            prev_l = l.replace("-B", "")
            group = [x[1]]
        else:
            if "-B" in l:
                grouped.append({"begin": last_border, "end": group[-1][-1], "type": prev_l})
                group = [x[1]]
                last_border = grouped[-1]["end"]
                prev_l = l.replace("-B", "")
            else:
                if l == prev_l:
                    group.append(x[1])
                else:
                    grouped.append({"begin": last_border, "end": group[-1][-1], "type": prev_l})
                    group = [x[1]]
                    last_border = grouped[-1]["end"]
                    prev_l = l.replace("-B", "")

    print(grouped)
    output = {"text": original_file["text"], "scenes": grouped}

    json.dump(output, open(out_dir, "w"))

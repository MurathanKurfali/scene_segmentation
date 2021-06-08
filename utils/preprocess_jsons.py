import os
import json
import shutil
import string
from collections import Counter
batch_size = 5

split_dict = {"9783732522033.json":"test.jsonl", "9783732557905.json": "dev.jsonl"}
all_labels = []
def read_json(json_file, out_dir):
    content = json.load(open(json_file, ))
    sentences, labels, selected = [], [], []
    scene_borders = {range(k["begin"], k["end"]): k["type"] for k in content["scenes"]}
    for sent in content["sentences"]:
        sentence = content["text"][sent["begin"]:sent["end"]]
        initial_punc_count = len(sentence) - len(sentence.lstrip(string.punctuation + " »"))
        label = None
        for k, v in scene_borders.items():
            if sent["begin"] + initial_punc_count in k:
                if k not in selected:
                    label = "{}-B".format(v)
                    selected.append(k)
                else:
                    label = v
                break
        if not label:
            label = "Nonscene"
        sentences.append(content["text"][sent["begin"]:sent["end"]])
        labels.append(label)
    all_labels.extend(labels)
    print(json_file, Counter(labels))
    split = split_dict.get(json_file.split("/")[-1], "train.jsonl")
    with open(os.path.join(out_dir, split), 'a+', encoding="utf8") as outfile:
        for index in range(0, len(sentences), batch_size):
            batch = {"abstract_id": 0}
            batch.update({"sentences": sentences[index:index + batch_size], "labels": labels[index:index + batch_size]})
            json.dump(batch, outfile)
            outfile.write('\n')


if __name__ == "__main__":
    raw_data = "../ebooks/json"
    out_dir = "../data/trial"
    if  os.path.exists(out_dir):
        shutil.rmtree(out_dir)
        os.makedirs(out_dir)

    raw_books = [os.path.join(raw_data, l) for l in os.listdir(raw_data)]
    for book in raw_books:
        # if "9783732596546" not in book: continue
        read_json(book, out_dir)
    print(Counter(all_labels))

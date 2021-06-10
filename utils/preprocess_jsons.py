import os
import json
import shutil
import string
from collections import Counter

batch_size = 12

split_dict = {"9783732522033.json": "test.jsonl", "9783732557905.json": "dev.jsonl"}
all_labels = []


def read_json(json_file, out_dir):
    content = json.load(open(json_file, ))
    sentences, labels,  = [], []
    selected = {"Scene": [], "Nonscene": []}
    scene_borders = {range(k["begin"], k["end"]): k["type"] for k in content["scenes"]}
    batch_length = []
    for sent in content["sentences"]:
        sentence = content["text"][sent["begin"]:sent["end"]]
        initial_punc_count = len(sentence) - len(sentence.lstrip(string.punctuation + " »"))
        sent_begin = sent["begin"] + initial_punc_count
        label = None
        for k, v in scene_borders.items():
            if sent_begin in k:
                if k not in selected[v]:
                    label = "{}-B".format(v)
                    selected[v].append(k)
                else:
                    label = v
                break
        if not label:
            label = "Nonscene"
            continue
        sentences.append(content["text"][sent["begin"]:sent["end"]])
        labels.append(label)
    all_labels.extend(labels)
    print(json_file, Counter(labels))
    split = split_dict.get(json_file.split("/")[-1], "train.jsonl")
    with open(os.path.join(out_dir, split), 'a+', encoding="utf8") as outfile:
        for index in range(0, len(sentences), batch_size):
            batch = {"abstract_id": 0}
            batch.update({"sentences": sentences[index:index + batch_size], "labels": labels[index:index + batch_size]})
            batch_length.append(len(" ".join(sentences[index:index + batch_size]).split()))
            #batch = {"labels": labels[index:index + batch_size]}
            json.dump(batch, outfile)
            outfile.write('\n')
    print(max(batch_length), min(batch_length))

if __name__ == "__main__":

    raw_data = "/home/murathan/Desktop/scene-segmentation/json" if "home/" in os.getcwd() else  "../ebooks/json"
    out_dir = "../data/trial"
    if os.path.exists(out_dir): shutil.rmtree(out_dir)
    os.makedirs(out_dir)

    raw_books = [os.path.join(raw_data, l) for l in os.listdir(raw_data)]
    for book in raw_books:
        #if "9783732557905" not in book: continue
        read_json(book, out_dir)
    total = sum(Counter(all_labels).values())
    print([ (k, total/v) for k,v in Counter(all_labels).items()])

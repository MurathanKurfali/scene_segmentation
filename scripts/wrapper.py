import json
import shutil
import sys

from allennlp.commands import main
import os

os.environ["SEED"] = "15270"
os.environ["PYTORCH_SEED"] = "1527"
os.environ["NUMPY_SEED"] = "1527"


# path to bert vocab and weights
os.environ["BERT_VOCAB"] = "https://ai2-s2-research.s3-us-west-2.amazonaws.com/scibert/allennlp_files/scivocab_uncased.vocab"
os.environ["BERT_WEIGHTS"] = "https://ai2-s2-research.s3-us-west-2.amazonaws.com/scibert/allennlp_files/scibert_scivocab_uncased.tar.gz"

# path to dataset files
os.environ["TRAIN_PATH"] = "data/CSAbstruct/train.jsonl"
os.environ["DEV_PATH"] = "data/CSAbstruct/dev.jsonl"
os.environ["TEST_PATH"] = "data/CSAbstruct/test.jsonl"


# model
os.environ["USE_SEP"] = "false"
os.environ["WITH_CRF"] = "false"

# training params
os.environ["cuda_device"] = "0"
os.environ["BATCH_SIZE"] = "4"
os.environ["LR"] = "5e-5"
os.environ["TRAINING_DATA_INSTANCES"] = "52"

os.environ["NUM_EPOCHS"] = "100"


# limit number of sentneces per examples, and number of words per sentence. This is dataset dependant
os.environ["MAX_SENT_PER_EXAMPLE"] = "10"
os.environ["SENT_MAX_LEN"] = "80"


# this is for the evaluation of the summarization dataset
os.environ["SCI_SUM"] = "false"
os.environ["USE_ABSTRACT_SCORES"] = "false"
os.environ["SCI_SUM_FAKE_SCORES"] = "false"

config_file = "sequential_sentence_classification/config.jsonnet"

# Use overrides to train on CPU.
overrides = json.dumps({"trainer": {"cuda_device": -1}})

serialization_dir = "/tmp/debugger_train"

# Training will fail if the serialization directory already
# has stuff in it. If you are running the same training loop
# over and over again for debugging purposes, it will.
# Hence we wipe it out in advance.
# BE VERY CAREFUL NOT TO DO THIS FOR ACTUAL TRAINING!
shutil.rmtree(serialization_dir, ignore_errors=True)

# Assemble the command into sys.argv
sys.argv = [
    "allennlp",  # command name, not used by main
    "train",
    config_file,
    "-s", serialization_dir,
    "--include-package", "sequential_sentence_classification",
    ]

main()
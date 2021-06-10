from allennlp.commands import train

if __name__ == "__main__":
    CONFIG_FILE = "sequential_sentence_classification/config.jsonnet"
    serialization = "xx"
    train.train_model(CONFIG_FILE, serialization)

    # python -m allennlp train $CONFIG_FILE  --include-package sequential_sentence_classification -s $SERIALIZATION_DIR "$@"

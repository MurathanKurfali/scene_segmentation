#!/bin/bash

export SEED=15270
export PYTORCH_SEED=`expr $SEED / 10`
export NUMPY_SEED=`expr $PYTORCH_SEED / 10`

# path to bert type and path
export BERT_MODEL=deepset/gbert-large
export TOKEN=[SEP]
export MODEL_TYPE=bert

# export BERT_MODEL=roberta-base
# export TOKEN="</s>"
# export MODEL_TYPE=roberta

# path to dataset files
export TRAIN_PATH=data/trial/train.jsonl
export DEV_PATH=data/trial/dev.jsonl
export TEST_PATH=data/trial/test.jsonl

# model
export USE_SEP=true  # true for our model. false for baseline
export WITH_CRF=false  # CRF only works for the baseline

# training params
export cuda_device=0
export BATCH_SIZE=4 # set one for roberta
export LR=2e-6
#export TRAINING_DATA_INSTANCES=1668
export TRAINING_STEPS=1000
export NUM_EPOCHS=50

# limit number of sentneces per examples, and number of words per sentence. This is dataset dependant
export MAX_SENT_PER_EXAMPLE=10
export SENT_MAX_LEN=60

# this is for the evaluation of the summarization dataset
export SCI_SUM=false
export USE_ABSTRACT_SCORES=false
export SCI_SUM_FAKE_SCORES=false  # use fake scores for testing

predict_file=data/predictions/pred.json
python -m allennlp predict xx data/trial/test.jsonl --output-file ${predict_file} --silent --use-dataset-reader --predictor SeqClassificationPredictor --include-package sequential_sentence_classification
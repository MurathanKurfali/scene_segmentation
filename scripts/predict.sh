#!/bin/bash

export SEED=15270
export PYTORCH_SEED=`expr $SEED / 10`
export NUMPY_SEED=`expr $PYTORCH_SEED / 10`

# path to bert type and path
export BERT_MODEL=deepset/gbert-large #bert-base-german-cased
export TOKEN=[SEP]
export MODEL_TYPE=bert

# export BERT_MODEL=roberta-base
# export TOKEN="</s>"
# export MODEL_TYPE=roberta

# path to dataset files
export TRAIN_PATH=data/ss/train.jsonl
export DEV_PATH=data/ss/dev.jsonl
export TEST_PATH=data/ss/test.jsonl

# model
export USE_SEP=true  # true for our model. false for baseline
export WITH_CRF=false  # CRF only works for the baseline

# training params
export cuda_device=0
export BATCH_SIZE=8 # set one for roberta
export LR=5e-6
#export TRAINING_DATA_INSTANCES=1668
export TRAINING_STEPS=1000
export NUM_EPOCHS=100

# limit number of sentences per examples, and number of words per sentence. This is dataset dependant


# this is for the evaluation of the summarization dataset
export SCI_SUM=false
export USE_ABSTRACT_SCORES=false
export SCI_SUM_FAKE_SCORES=false  # use fake scores for testing


model=$1
test_file=$2
output_file=$3
output_file="data/predictions/${output_file}.pred"
python -m allennlp predict "${model}" "${test_file}" --output-file "${output_file}" --silent  --use-dataset-reader --predictor SeqClassificationPredictor --include-package sequential_sentence_classification

#!/bin/bash

model=$1
test_file=$2
output_file=$3
output_file="predictions/${output_file}.pred"
python -m allennlp predict  "${model}" "${test_file}" --output-file "${output_file}" --silence  --use-dataset-reader --predictor SeqClassificationPredictor --include-package code.sequential_sentence_classification --cuda-device 0

#!/bin/bash

model=$1
test_file=$2
output_file=$3

echo "Running the model on ${test_file}"
python -m allennlp predict  "${model}" "${test_file}" --output-file "${output_file}" --silent  --use-dataset-reader --predictor SeqClassificationPredictor --include-package src.sequential_sentence_classification --cuda-device 0
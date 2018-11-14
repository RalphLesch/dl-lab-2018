#!/bin/sh
python3 cnn_mnist.py --learning_rate=0.1 --run_id=21
python3 cnn_mnist.py --learning_rate=0.01 --run_id=201
python3 cnn_mnist.py --learning_rate=0.001 --run_id=2001
python3 cnn_mnist.py --learning_rate=0.0001 --run_id=20001

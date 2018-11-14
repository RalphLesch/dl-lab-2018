#!/bin/sh
for i in 1 3 5 7 ; do python3 cnn_mnist.py --filter_size=$i --run_id=3$i ; done

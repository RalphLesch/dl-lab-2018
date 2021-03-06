#!/bin/bash
if [ -z "$1" ]; then
    format='pdf'
else
    format=$1
fi

# Plot all
labels=()
for i in {4..1}; do
    python3 plot.py code/checkpoints/ultraslimS_$i/testIoU.txt -x epoch -y IoU -n -c $((4-i)) -o plots/config$i.$format -f $format
    inputs="$inputs code/checkpoints/ultraslimS_$i/testIoU.txt"
    labels+=("config $i")
done
python3 plot.py $inputs -l "${labels[@]}" -x epoch -y IoU -m -n -o plots/configs -f $format

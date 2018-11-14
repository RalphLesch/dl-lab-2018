#!/bin/sh

# Plot all
# python3 plot_results.py results/results_run_* -o results/plots -f png -n

# plot for #1
#python3 plot_results.py results/results_run_1.json -o results/plots -n -f png
python3 plot_results.py results/results_run_1.json -o results/plots -n -f pdf

# plot for #2
# together
#python3 plot_results.py results/results_run_2* -o results/plots/plot_2 -n -m -l 0.0001 0.001 0.01 0.1 -f png
python3 plot_results.py results/results_run_2* -o results/plots/plot_2 -n -m -l 0.0001 0.001 0.01 0.1 -f pdf

# single, preserving color like above
#python3 plot_results.py results/results_run_2* -o results/plots -c -n -f png
python3 plot_results.py results/results_run_2* -o results/plots -c -n -f pdf

# only 0.01 and 0.1 together while using the same colors like in the full plot
python3 plot_results.py results/results_run_201.json results/results_run_21.json  -o results/plots/plot_2_1_01 -n -c 2 -m -l 0.01 0.1 -f pdf
#python3 plot_results.py results/results_run_201.json results/results_run_21.json  -o results/plots/plot_2_1_01 -n -c 2 -m -l 0.01 0.1 -f png

# plot for #3
python3 plot_results.py results/results_run_3* -o results/plots/plot_3 -n -f pdf -m -l 1 3 5 7

# plot for #4
python3 plot_results.py results/results_run_random_search.json -o results/plots -f -n pdf

# Plot results

import argparse
import sys
import os
import glob
import json
import matplotlib.pyplot as plt

def get_json_data(file):
    with open(file) as f:
        results = json.load(f)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, nargs='+',
                        help='result json file(s)')
    parser.add_argument('-t', '--title', type=str, nargs='*',
                        help='title of the plot, defaults to filename')
    parser.add_argument('-y', '--ylabel', type=str, nargs='?',
                        help='y label', default='error')
    parser.add_argument('-x', '--xlabel', type=str, nargs='?',
                        help='x label', default='epoch')
    parser.add_argument('-o', '--output', type=str, nargs='?',
                        help='save to output folder or file, defaults to title.format',
                        metavar='PATH', const='')
    parser.add_argument('-f', '--format', type=str, nargs='?',
                        help='output format, defaults to png', default='png')
    parser.add_argument('-n', '--noplot', action='store_true',
                        help='do not show plot')
    parser.add_argument('-m', '--merge', action='store_true',
                        help='merge plots into one')
    parser.add_argument('-l', '--labels', nargs='+',
                        help='labels for in a merge plot')
    parser.add_argument('-c', '--color', type=int, nargs='?',
                        help='preserve the color in single plots like in merged plot, starting with COLOR_INDEX', metavar='COLOR_INDEX', default=0)
    args = parser.parse_args()
    
    if args.file:
        if len(args.file) == 1:
            args.file = glob.glob(args.file[0]) or args.file
            
        if args.title == []:
            args.title = (os.path.splitext(os.path.basename(f))[0] for f in args.file)
        elif not args.title:
            args.title = (False for f in args.file)
        
        if not args.labels:
            args.labels = (False for f in args.file)
        
        if args.color and args.merge:
            for x in range(args.color):
                plt.plot([], [])
        
        for i, (file, title, label) in enumerate(zip(args.file, args.title, args.labels)):
            result_json = get_json_data(file)
            
            extra = {'label': label} if label else {}
            if args.merge:
                print('adding {} as {}'.format(file, label))
                plt.plot(result_json['learning_curve'], **extra)
            else:
                plt.figure()
                plt.ylabel(args.ylabel)
                plt.xlabel(args.xlabel)
                if title:
                    plt.title(title)
                
                if args.color:
                    for _ in range(i + args.color):
                        plt.plot([], [])
                
                plt.plot(result_json['learning_curve'], **extra)
                if args.output or args.output == '':
                    if os.path.isdir(args.output):
                        outputPath = args.output
                        outputName = title or os.path.splitext(os.path.basename(file))[0]
                    else:
                        outputPath = ''
                        outputName = title or os.path.splitext(file)[0]
                    outputName = os.path.join(outputPath, outputName)
                    outputName = '{}.{}'.format(outputName, args.format)
                    print('Saving ' + outputName)
                    plt.savefig(outputName)
                if not args.noplot:
                    print('Showing', title or file, sep=' ')
                    plt.show()
        if args.merge:
            plt.legend()
            if args.output or args.output == '':
                outputName = '{}.{}'.format((args.output or title or os.path.splitext(args.file[0])[0] + '_merged'), args.format)
                print('Saving ' + outputName)
                plt.savefig(outputName)
            if not args.noplot:
                print('Showing', title or file, sep=' ')
                plt.show()
            
            

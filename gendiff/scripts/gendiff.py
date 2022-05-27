#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str, help='')
parser.add_argument('second_file', type=str, help='')
parser.add_argument('-f', '--format', default=1, help = 'set format of output')
args = parser.parse_args()




def main():
    print("Welcome!!!!")
    print(args)
    f = args.format
    print(f)
    

if __name__ == '__main__':
    main()

#!/usr/bin/env python
import json
from gendiff.scripts import generate_diff
def parse():
    import argparse
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', default=1, help = 'set format of output')
    args = parser.parse_args()
    return args


def main():
    args_diff = parse()
    print("Welcome!!!!")
    with open(args_diff.first_file) as file:
        data = file.read()
        f1 = json.loads(data)  
    with open(args_diff.second_file) as file:
        data = file.read()
        f2 = json.loads(data)
    out = (generate_diff(f1, f2))
    print(out)
    out1 = json.dumps(out)
    # print(out1)
    with open('output.json', 'w') as file_to_write: 
        json.dump(out, file_to_write)
    

if __name__ == '__main__':
    main()

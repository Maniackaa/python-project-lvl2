#!/usr/bin/env python
import json
import yaml
from yaml import CLoader as Loader
from ..generate_diff import generate_diff
from ..parse import parse


def main():
    args_diff = parse()
    file1 = args_diff.first_file
    file2 = args_diff.second_file
    print("Welcome!!!!")
    with open(args_diff.first_file) as file:
        data = file.read()
        if file1.endswith('.yml'):
            f1 = yaml.load(data, Loader=Loader)
        elif file1.endswith('.json'):
            f1 = json.loads(data)

    with open(args_diff.second_file) as file:
        data = file.read()
        if file2.endswith('.yml'):
            f2 = yaml.load(data, Loader=Loader)
        elif file1.endswith('.json'):
            f2 = json.loads(data)
    out = (generate_diff(f1, f2))
    print(out)
    # out1 = json.dumps(out)
    # print(out1)
    with open('output.txt', 'w') as file_to_write:
        # json.dump(out, file_to_write)
        file_to_write.write(out)


if __name__ == '__main__':
    main()

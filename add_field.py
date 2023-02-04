from pathlib import Path
import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-data', help="JSON file from which data is loaded and saved",
                        type=Path, required=True)
    parser.add_argument('-key', help="The key to be inserted", type=str, required=True)
    parser.add_argument('-val', help="The value to be inserted for every key")
    parser.add_argument('-loc', help="Specifies the key of the dict where the desired key is inserted")
    parser.add_argument('-rec', action='store_true',
                        help="Specifies if keys are added recursively if location is not provided")
    return parser.parse_args()


def add(parser):
    with open(parser.data, 'r') as json_file:
        data = json.load(json_file)

    def loop(dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                if parser.loc is None or key == parser.loc:
                    value.setdefault(parser.key, parser.val)
                if parser.rec or parser.loc:
                    loop(value)

    loop({'data': data})
    # loop(data)   # this way ignores the first layer of elements
    with open(parser.data, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    add(parse_args())

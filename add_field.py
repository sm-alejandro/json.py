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


def add(data: dict, loc: str, key: str, val, rec: bool):
    def loop(dictionary):
        for key_, value_ in dictionary.items():
            if isinstance(value_, dict):
                if loc is None or key_ == loc:
                    value_.setdefault(key, val)
                if rec or loc:
                    loop(value_)
    loop(data)
    return data


if __name__ == "__main__":
    parser = parse_args()
    with open(parser.data, 'r') as json_file:
        json_data = json.load(json_file)

    result = add(data=json_data, loc=parser.loc, key=parser.key, val=parser.val, rec=parser.rec)

    with open(parser.data, 'w') as json_file:
        json.dump(result, json_file)

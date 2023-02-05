from pathlib import Path
import argparse
import json
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-data', help="JSON file from which data is loaded and saved",
                        type=Path, required=True)
    parser.add_argument('-key', help="OrigKey=NewKey value pairs",
                        nargs='*', type=str, required=True)
    parser.add_argument('-rec', action='store_true',
                        help="Specifies if all the document is affected")
    return parser.parse_args()


def replace(data: dict, key: dict, loc: str, rec: bool):
    def loop(dictionary):
        for key_, value_ in dictionary.items():
            if isinstance(value_, dict):
                print(loc)
                if not loc or re.match(loc, key_):
                    for k in key:
                        if k in value_:
                            value_[key[k]] = value_.pop(k)
                if rec or loc:
                    loop(value_)
    loop(data)
    return data


if __name__ == "__main__":
    parser = parse_args()
    with open(parser.data, 'r') as json_file:
        json_data = json.load(json_file)

    replace_dict = {}
    for x in parser.key:
        key, value = x.split('=')
        replace_dict[key] = value
    result = replace(data=json_data, key=replace_dict, rec=parser.rec)

    with open(parser.data, 'w') as json_file:
        json.dump(result, json_file)

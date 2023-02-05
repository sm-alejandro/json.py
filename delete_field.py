from pathlib import Path
import argparse
import json
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-data', help="JSON file from which data is loaded and saved",
                        type=Path, required=True)
    parser.add_argument('-key', help="The key to be removed",
                        type=str, required=True)
    parser.add_argument(
        '-loc', help="Specifies the key of the dict where the desired key is removed")
    parser.add_argument('-rec', action='store_true',
                        help="Specifies if keys are added recursively if location is not provided")
    return parser.parse_args()


def delete(data: dict, loc: str, key: str, rec: bool):
    def loop(dictionary):
        for key_, value_ in dictionary.items():
            if isinstance(value_, dict):
                if loc is None or re.match(loc, key_):
                    try:
                        del value_[key]
                    except Exception:
                        pass
                if rec or loc:
                    loop(value_)

    loop(data)
    return data


if __name__ == "__main__":
    parser = parse_args()
    with open(parser.data, 'r') as json_file:
        json_data = json.load(json_file)

    result = delete(data=json_data, loc=parser.loc,
                    key=parser.key, rec=parser.rec)

    with open(parser.data, 'w') as json_file:
        json.dump(result, json_file)

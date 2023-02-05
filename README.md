# JSON_HELPER.py
Functions to bulk add/delete/modify json fields

# PACKAGE USAGE
import bulkjson

bulkjson.add(data: dict, loc: str, key: str, val, rec: bool)

bulkjson.delete(data: dict, loc: str, key: str, rec: bool):

bulkjson.replace(data: dict, loc: str, key: dict, rec: bool):

# CONSOLE USAGE (operations on example.json)

## ADD
Simple additions (adding to every key in the root of the document):
>py ./add_field.py -data ./data/example.json -key "timestamp"

Recursive additions (adding to every possible dictionary)
> py ./add_field.py -data ./data/example.json -key "custom" -rec

Add to specific key
> py ./add_field.py -data ./data/example.json -key "direction" -loc "wind"


## DELETE
Simple deletions (deleting from every key in the root of the document):
> py ./delete_field.py -data ./data/example.json -key "wind"

Recursive deletions (deleting from every possible dictionary)
> py ./delete_field.py -data ./data/example.json -key "speed" -rec

Remove from certain key
> py ./delete_field.py -data ./data/example.json -key "speed" -loc "wind"


## REPLACE
Simple replacements (replacing from every key in the root of the document):
> py ./replace_field.py -data ./data/example.json -key "{'measurement_2': 'measurement_4'}"

Recursive replacements (replacing from every possible dictionary)
> py ./replace_field.py -data ./data/example.json -key {'wind': 'temperature'} -rec

Remove from certain key
> py ./replace_field.py -data ./data/example.json -key {'speed': 'quantity'} -loc "rain"


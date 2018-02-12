import json
import sys

filepath = sys.argv[1]


def load_data(filepath):
    load_json = json.load(open(str(filepath)))
    return load_json

data = load_data(filepath)

def pretty_print_json(data):
    parse_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': '))
    return parse_json

print (pretty_print_json(data))

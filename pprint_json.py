import json
import sys

filepath = sys.argv[1]


def load_data(filepath):
    data = json.load(open(str(filepath)))
    return data

data = load_data(filepath)

def pretty_print_json(data):
    my_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': '))
    return my_json

print (pretty_print_json(data))

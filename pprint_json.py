import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except ValueError as error:
        return None


def pretty_print_json(json_load):
    json_pretty = json.dumps(
        json_load,
        indent=4,
        ensure_ascii=False,
        separators=(',', ': '))
    print(json_pretty)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        json_load = load_data(filepath)
    except IndexError as error:
        sys.exit('Not set argyment filepath')
    except FileNotFoundError as error:
        sys.exit('File not found')
    else:
        pretty_print_json(json_load)

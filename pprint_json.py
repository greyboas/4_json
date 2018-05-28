import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except ValueError as error:
        return None


def pretty_print_json(loaded_json):
    pretty_json = json.dumps(
        loaded_json,
        indent=4,
        ensure_ascii=False,
        separators=(',', ': '))
    print(pretty_json)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        loaded_json = load_data(filepath)
    except IndexError:
        sys.exit('Not set argyment filepath')
    except FileNotFoundError:
        sys.exit('File not found')
    else:
        pretty_print_json(loaded_json)

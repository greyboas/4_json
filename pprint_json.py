import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except ValueError as error:
        return 'It is not file fotmat JSON'


def pretty_print_json(data):
    json_viewer = json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
        separators=(',', ': '))
    print(json_viewer)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        file = open(filepath)
    except IndexError as error:
        print('Not set argyment filepath')
        sys.exit(-1)
    except FileNotFoundError as error:
        print('File not found: ', error)
        sys.exit(-1)
    else:
        data = load_data(filepath)
        pretty_print_json(data)

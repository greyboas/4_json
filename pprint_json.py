import json
import sys


def load_data(filepath):
        try:
            with open(filepath, 'r') as file_handler:
                return json.load(file_handler)
        except FileNotFoundError as error:
            print('File not found: ', error)
        except ValueError as error:
            print('Json code unccorect or file not format json. Error: ', error)


def pretty_print_json(filepath):
    data = load_data(filepath)
    parse_text = json.dumps(data, indent=4,
                            ensure_ascii=False, separators=(',', ': '))
    print(parse_text)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError as error:
        filepath = 'example_bar.json'
    pretty_print_json(filepath)

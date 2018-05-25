import json
import sys

def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except ValueError as error:
        print('Json code unccorect or file not format json. Error: ', error)
    except FileNotFoundError as error:
        print('File not found: ', error)

def pretty_print_json(filepath):
    json_data = load_data(filepath)
    parse_json = json.dumps(json_data, indent=4, ensure_ascii=False, separators=(',', ': '))
    return parse_json

if __name__ == '__main__':
    filepath = sys.argv[1]
    print (pretty_print_json(filepath))





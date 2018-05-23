import json
import sys


filepath = sys.argv[1]


def pretty_print_json(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return  json.dumps(json.load(file_handler), indent=4, ensure_ascii=False, separators=(',', ': '))
    except ValueError as e:
        print('Json code unccorect or file not format json. Error: ', e)

if __name__ == '__main__':
    print (pretty_print_json(filepath))




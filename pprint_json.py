import json
import sys


filepath = sys.argv[1]

try:
    def load_data(filepath):
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)

    def pretty_print_json(filepath):
        json_data = load_data(filepath)
        parse_json = json.dumps(json_data, indent=4, ensure_ascii=False, separators=(',', ': '))
        return parse_json

    if __name__ == '__main__':
        print (pretty_print_json(filepath))


except ValueError as e:
    print ('Json code unccorect or file not format json. Error: ',e)




# recursivejson.py

import json

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

data_file = open('responses_bulk.json','r').read()
json_data = json.loads(data_file)

names = extract_values(json_data, 'text')

print (names)


for name in names:
    x = name.encode('utf-8')
    print (x.decode('unicode-escape'))

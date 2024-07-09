import json

def read_json_recursive(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_json(data):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"Key: {key}")
            read_json(value)
    elif isinstance(data, list):
        for item in data:
            read_json(item)
    else: # if data is value 
        print(f"Value: {data}")

if __name__ == "__main__":
    file_path = 'data/data.json'
    data = read_json_recursive(file_path)
    read_json(data)

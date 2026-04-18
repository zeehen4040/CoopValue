import json
def read_jsonl(filename):
    with open(filename, 'r') as f:
        return [json.loads(line) for line in f]
    
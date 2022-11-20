import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(file, delimiter=',') -> list[dict]:
    with open(file, encoding='utf-8') as f:
        lst_ = []
        headers = f.readline().replace('\n', "").split(delimiter)
        for line in f:
            line_new = line.replace('\n', "").split(delimiter)
            lst_ += [dict(zip(headers, line_new)) for elem in range(1)]
        return lst_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

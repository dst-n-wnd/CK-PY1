import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=',') -> list[dict]:
    with open(file, encoding='utf-8') as f:
        lst_ = []
        headers = f.readline().strip().split(delimiter)
        for line in f:
            if line.strip().split(delimiter) != headers:
                line_new = line.strip().split(delimiter)
                lst_ += [dict(zip(headers, line_new)) for elem in range(1)]
        return lst_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

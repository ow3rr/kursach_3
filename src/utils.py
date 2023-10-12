from typing import List, Dict
import json
import os.path

json_path = os.path.join('../data/operations.json')


def load_operations_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        temp_file = json.load(file)
        list_operaions = []
        for f in temp_file:
            if f == {}:
                continue
            else:
                list_operaions.append(f)
        return list_operaions


def filter_and_sort(data: List[Dict]) -> List[Dict]:
    filtered_data = [item for item in data if item.get('state') == 'EXECUTED']
    sorted_data = sorted(filtered_data, key=lambda x: x.get('date'), reverse=True)
    return sorted_data[:5]


def get_date(date: str) -> str:
    dt = date[0:10].split(sep='-')
    return f'{dt[2]}.{dt[1]}.{dt[0]}'


def mask_card_num_from(msg: str) -> str:
    arr = msg.split()[-1]
    if len(arr) == 16:
        arr_card_num = arr[0:4] + " " + arr[4:6] + "*" * 2 + " " + "*" * 4 + " " + arr[12:16]
        return arr_card_num
    elif len(arr) == 20:
        arr_account_num = "**" + arr[-4:]
        return arr_account_num


def mask_card_num_to(msg: str) -> str:
    arr = msg.split()[-1]
    if len(arr) == 16:
        arr_card_num = arr[0:4] + " " + arr[5:7] + "*" * 2 + " " + "*" * 4 + " " + arr[12:16]
        return arr_card_num
    elif len(arr) == 20:
        arr_account_num = "**" + arr[-4:]
        return arr_account_num


def final_mask():
    list_operations = load_operations_json(json_path)
    for operation in filter_and_sort(list_operations):
        print(f"{get_date(operation['date'])} {operation['description']}")
        if 'from' not in operation:  # если нет ключа 'from'
            card = operation['to'].split()
            card_num_to = card[-1]
            num_to = mask_card_num_to(card_num_to)
            print(f"-> {' '.join(card[:-1])} {num_to}")
        else:
            card = operation['to'].split()
            card_num_to = card[-1]
            num_to = mask_card_num_to(card_num_to)
            card_from = operation['from'].split()
            card_num_from = card_from[-1]
            num_from = mask_card_num_from(card_num_from)
            print(f"{' '.join(card_from[:-1])} {num_from} -> {' '.join(card[:-1])} {num_to}")

        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")

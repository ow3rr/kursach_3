import pytest
import os.path
import json

from src.utils import (
    load_operations_json,
    filter_and_sort,
    get_date,
    mask_card_num_from,
    mask_card_num_to,
    final_mask,
)

json_path = os.path.join('../data/operations.json')


def test_load_operations_jsonsample_data(sample_data):

    json_path = "../data/operations.json"  # Replace with the actual path to your operations.json file
    operations = load_operations_json(json_path)
    assert operations == sample_data


def test_filter_and_sort(sample_data):
    filtered_data = filter_and_sort(sample_data)
    assert len(filtered_data) == 5
    assert filtered_data[0]["state"] == "EXECUTED"
    assert filtered_data[0]["date"] == "2019-08-26T10:50:58.294041"


def test_get_date():
    date = "2019-08-26T10:50:58.294041"
    formatted_date = get_date(date)
    assert formatted_date == "26.08.2019"


def test_mask_card_num_from():
    card_num = "Maestro 7810846596785568"
    masked_num = mask_card_num_from(card_num)
    assert masked_num == "7810 84** **** 5568"


def test_mask_card_num_to():
    card_num = "Счет 64686473678894779589"
    masked_num = mask_card_num_to(card_num)
    assert masked_num == "**9589"

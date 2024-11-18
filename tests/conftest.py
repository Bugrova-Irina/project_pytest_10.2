from typing import Any

import pytest


@pytest.fixture
def invalid_len_number() -> str:
    return "1254646"


@pytest.fixture
def letter_number() -> str:
    return "sdsfdsgdf"


@pytest.fixture
def empty_number() -> str:
    return ""


@pytest.fixture
def invalid_len_date() -> str:
    return "2024-03-11T02:26:18.67140"


@pytest.fixture
def empty_date() -> str:
    return ""


@pytest.fixture
def letter_card_number() -> str:
    return "master sdsfdsgdf"


@pytest.fixture
def list_of_dicts_with_invalid_status() -> list[dict[str, Any]]:
    return [{'id': 41428829, 'state': 'fgd', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': '', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'dff', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'sgdh', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def list_of_dicts_with_invalid_dates() -> list[dict[str, Any]]:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': 'dd19-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': 'sss-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': 'qww-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2015-10-14T08:21:33.419441'}]

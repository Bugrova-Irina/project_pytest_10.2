import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("list_of_dicts, state, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     'EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     'CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])


def test_filter_by_state(list_of_dicts, state, expected):
    assert filter_by_state(list_of_dicts, state) == expected


def test_filter_by_state_empty_dict():
    with pytest.raises(ValueError):
        filter_by_state([{}])


def test_filter_by_invalid_state(list_of_dicts_with_invalid_status):
    with pytest.raises(ValueError):
        filter_by_state(list_of_dicts_with_invalid_status)


@pytest.mark.parametrize("list_of_dicts, reverse, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
])


def test_sort_by_date(list_of_dicts, reverse, expected):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], reverse) == expected


@pytest.mark.parametrize("list_of_dicts, reverse, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'}],
     False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
])


def test_sort_by_same_date(list_of_dicts, reverse, expected):
    assert sort_by_date(list_of_dicts, reverse) == expected


def test_sort_by_invalid_date(list_of_dicts_with_invalid_dates):
    with pytest.raises(ValueError):
        sort_by_date(list_of_dicts_with_invalid_dates)


def test_filter_by_empty_date():
    with pytest.raises(ValueError):
        sort_by_date([{}])
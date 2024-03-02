from src.utils import last_operation, sort_date
from src.class_operation import Operation

from_ = {'from': 'Visa Gold 3654412434951162',
             'to': 'Счет 59986621134048778289'}
to_ = {'to': 'Счет 6468647367889477958'}
date_ = {'date': '2019-08-26T10:50:58.294041',
        'description': 'Перевод организации'}
amount_ = {'operationAmount': {'amount': '8221.37',
                               'currency': {'name': 'USD',
                                            'code': 'USD'}}}

def test_class():
    assert Operation(from_).from_to() == "Visa Gold  3654 41** **** 1162  -> Счет **8289"
    assert Operation(to_).from_to() == "Счет **7958"
    assert Operation(date_).date() == "26.08.2019 Перевод организации"
    assert Operation(amount_).amount() == "8221.37 USD"

test_date = [
    {'date': '2018-12-22T02:02:49.564873'},
    {'date': '2019-01-05T00:52:30.108534'},
    {'date': '2019-07-13T18:51:29.313309'},]

def test_sort_date():
    assert sort_date(test_date) == [
        {'date': '2019-07-13T18:51:29.313309'},
        {'date': '2019-01-05T00:52:30.108534'},
        {'date': '2018-12-22T02:02:49.564873'},]

test_operation = [
    {'state': 'CANCELED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'}]


def test_last_operation():
    assert last_operation(test_operation) == [
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},]

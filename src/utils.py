import json

def open_js(file_name):
    with open(file_name, 'r', encoding="utf8") as file:
        operations = file.read()
        json_file = json.loads(operations)
        return json_file

def sort_date(json_file):
    """Сортировка операций по дате"""
    operations_list = []
    for item in json_file:
        if item:
            operations_list.append(item)
    list_date = sorted(operations_list, key=lambda x: x['date'], reverse=True)
    return list_date


def last_operation(list_date):
    """Вывод 5 выполненных (EXECUTED) операций выведены на экран."""
    sorted_lst = []
    for item in list_date:
        if item ['state'] == 'EXECUTED':
            sorted_lst.append(item)
            if len(sorted_lst) == 5:
                break
    return sorted_lst
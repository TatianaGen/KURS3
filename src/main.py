from src.utils import open_js, last_operation, sort_date
from class_operation import Operation

j = open_js("operations.json")
list_date = sort_date(j)
last_operations = last_operation(list_date)
"""Список 5 одобренных операций"""
sort_list = last_operation(list_date)
"""Цикл для вывода операций в нужном формате"""
for i in sort_list:
    gg = Operation(i)
    print(gg.date())
    print(gg.from_to())
    print(f"""{gg.amount()})
    """)
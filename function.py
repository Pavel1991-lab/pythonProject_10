"""
import json
from datetime import datetime

"Функция которая переводим джейсон файл в список"
def execute(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    execute = []
    for i in data:
            execute.append(i)
    return execute




"Функция которая делаеет список в котором будут только пройденые операции"
def filter_by_state(lst):
    new_lst = []
    for item in lst:
        if 'state' in item and item['state'] == 'EXECUTED':
            new_lst.append(item)
    return new_lst


"Функция которая сортирует спиосок по дате в порядке убывания"
def sort_by_date(lst):
    return sorted(lst, key=lambda x: x['date'], reverse=True)



"Функция которая делает список из пяти самых свежих операций"
def print_first_five_operations(lst):
    first_five_operations = lst[:5]
    return  first_five_operations



"Функция которая получает первую операцию и все что с ней связано"
def get_first_id_info(lst):
    first_operation = lst[0]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info

"Функция которая получает вторую операцию и все что с ней связано"
def get_second_id_info(lst):
    first_operation = lst[1]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info

"Функция которая получает третию операцию и все что с ней связано"
def get_third_id_info(lst):
    first_operation = lst[2]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info

"Функция которая получает четвертую операцию и все что с ней связано"
def get_fourth_id_info(lst):
    first_operation = lst[3]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info

"Функция которая получает пятую операцию и все что с ней связано"
def get_five_id_info(lst):
    first_operation = lst[4]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info

"Функция которая получает описание опреции"
def get_description(data):
    return data[0]['description']

"Функция которая получает дату операции"
def get_date(data):
    date = data[0]['date']
    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_obj.strftime('%d.%m.%Y')

"Функция которая получает счет куда переводим деньги"
def get_to(accounts):
    for account in accounts:
        to = account['to']
    last_four = to[-4:]
    formatted = f"Счет **{last_four}"
    return formatted

"Функция которая получает количество денег участвующих в операции"
def get_amount_from_list(transactions):
    amounts = []
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError('Input parameter must be a list of dictionaries')
        if 'operationAmount' in transaction and isinstance(transaction['operationAmount'], dict) and 'amount' in transaction['operationAmount']:
            amounts.append(float(transaction['operationAmount']['amount']))
        for i in amounts:
            return i

"Функция которая получает информцию откуда переводили деньги"
def gettofromlist(self):
    for transaction in self.get_first_id_info():
        if 'from' in transaction and transaction['from'] is not None:
            list = transaction['from'].split()
            if len(list) >= 3 and 'Счет' not in list:
                return f'{list[0]} {list[1]} {list[2][0:4]} {list[2][4:6]}** **** {list[2][11:]}'
            elif len(list) < 3 and 'Счет' not in list:
                return f'{list[0]} {list[1][4:6]}** **** {list[1][11:]}'
            elif len(list) < 3 and 'Счет' in list:
                return f'Счет **{list[1][16:]}'
    return ''

"""


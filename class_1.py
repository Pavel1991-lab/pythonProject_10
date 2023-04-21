import json
from datetime import datetime

class Oper:
    def __init__(self, list, count:int):
        self.list = list
        self.count = count

    def execute(self):
        with open(self.list, 'r', encoding='utf-8') as f:
            data = json.load(f)
        execute = []
        for i in data:
            execute.append(i)
        return execute

    def filter_by_state(self):
        new_lst = []
        for item in self.execute():
            if 'state' in item and item['state'] == 'EXECUTED':
                new_lst.append(item)
        return new_lst

    def sort_by_date(self):
        data = self.filter_by_state()
        data_with_date = [x for x in data if 'date' in x]
        return sorted(data_with_date, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    def print_first_five_operations(self):
        first_five_operations = self.sort_by_date()[:self.count]
        return first_five_operations

    def get_first_id_info(self):
        first_operations = self.print_first_five_operations()
        if first_operations:
            if self.count <= len(first_operations):
                first_operation = first_operations[self.count - 1]
                if isinstance(first_operation, dict) and 'id' in first_operation:
                    first_id = first_operation['id']
                    first_id_info = [operation for operation in first_operations if operation.get('id') == first_id]
                    return first_id_info
        return []

    def get_description(self):
        return self.get_first_id_info()[0]['description']

    def get_date(self):
        date = self.get_first_id_info()[0]['date']
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        return date_obj.strftime('%d.%m.%Y')

    def get_to(self):
        for account in self.get_first_id_info():
            to = account['to']
        last_four = to[-4:]
        formatted = f"Счет **{last_four}"
        return formatted

    def get_amount_from_list(self):
        amounts = []
        for transaction in self.get_first_id_info():
            if not isinstance(transaction, dict):
                raise TypeError('Input parameter must be a list of dictionaries')
            if 'operationAmount' in transaction and isinstance(transaction['operationAmount'], dict) and 'amount' in \
                    transaction['operationAmount']:
                amounts.append(float(transaction['operationAmount']['amount']))
            for i in amounts:
                return i

    def gettofromlist(self):
        for transaction in self.get_first_id_info():
            if 'from' in transaction and transaction['from'] is not None:
                list = transaction['from'].split()
                if len(list) >=3 and 'Счет' not in list:
                    return f'{list[0]} {list[1]} {list[2][0:4]} {list[2][4:6]}** **** {list[2][11:]}'
                elif len(list)<3 and 'Счет' not in list:
                    return f'{list[0]} {list[1][0:4]} {list[1][4:6]}** **** {list[1][11:]}'
                elif len(list) <3 and 'Счет' in list:
                    return f'Счет **{list[1][16:]}'
        return ''




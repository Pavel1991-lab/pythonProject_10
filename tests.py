from datetime import datetime

from class_1 import Oper


import pytest
three = [ {
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
      "amount": "30153.72",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 7810846596785568",
    "to": "Счет 43241152692663622869"
  }
]

@pytest.fixture
def oper():
    return Oper('operations.json', 3)


def test_execute(oper):
    assert isinstance(oper.execute(), list)

def test_filter_by_state(oper):
    assert all(item['state'] == 'EXECUTED' for item in oper.filter_by_state())

def test_sort_by_date(oper):
    sorted_list = oper.sort_by_date()
    assert sorted_list == sorted(sorted_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

def test_print_first_five_operations(oper):
    five = oper.print_first_five_operations()
    assert five == oper.sort_by_date()[:3]

def test_get_first_id_info(oper):
    first = oper.get_first_id_info()
    assert first == three

def test_get_description(oper):
    des = oper.get_description()
    assert des == oper.get_first_id_info()[0]['description']

def test_get_date(oper):
    date = oper.get_first_id_info()[0]['date']
    assert date == '2019-11-19T09:22:25.899614'

def test_get_to(oper):
    to = oper.get_to()
    assert to == "Счет **2869"

def test_get_amount_from_list(oper):
    money = oper.get_amount_from_list()
    assert money == 30153.72

def test_gettofromlist(oper):
    fro = oper.gettofromlist()
    assert fro == 'Maestro 7810 84** **** 85568'






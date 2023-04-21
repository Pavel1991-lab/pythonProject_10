from class_1 import Oper



for i in range(1,20):
    Operation = Oper('operations.json', i)
    fro = Operation.gettofromlist()
    des = Operation.get_description()
    dat = Operation.get_date()
    t = Operation.get_to()
    amoun =  Operation.get_amount_from_list()
    print(f'{dat} {des} \n{fro} -> {t} \n{amoun}')
    print()







"""
from function import get_date, get_description, gettofromlist, get_to, get_amount_from_list, get_first_id_info, \
    get_second_id_info, get_fourth_id_info, get_third_id_info, get_five_id_info, sort_by_date, filter_by_state, execute, \
    print_first_five_operations

"Переводим json файл в список"
list =  execute('C:/Users/Алексей/PycharmProjects/pythonProject92/operations.json')

"Получаем список только с пройдеными операциями(execute)"
new_c = filter_by_state(list)


"Получаем список где все операции идут по порядку по дате(по убыванию)"
sort_data = sort_by_date(new_c)


"Из списка который идет по порядку, оставляем пять самых свежих операций"
first_five = print_first_five_operations(sort_data)


"Получаем списки пяти самых свежих функций"
one = get_first_id_info(first_five)
two = get_second_id_info(first_five)
three = get_third_id_info(first_five)
four = get_fourth_id_info(first_five)
five = get_five_id_info(first_five)


print(f'{get_date(one)} {get_description(one)} \n{gettofromlist(one)} -> {get_to(one)} \n{get_amount_from_list(one)}')
print()
print(f'{get_date(two)} {get_description(two)} \n{gettofromlist(two)} -> {get_to(two)} \n{get_amount_from_list(two)}')
print()
print(f'{get_date(three)} {get_description(three)} \n{gettofromlist(three)} -> {get_to(three)} \n{get_amount_from_list(three)}')
print()
print(f'{get_date(four)} {get_description(four)} \n{gettofromlist(four)} -> {get_to(four)} \n{get_amount_from_list(four)}')
print()
print(f'{get_date(five)} {get_description(five)} \n{gettofromlist(five)} -> {get_to(five)} \n{get_amount_from_list(five)}')
"""






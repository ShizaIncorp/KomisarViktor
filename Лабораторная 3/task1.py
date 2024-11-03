# TODO Напишите функцию для поиска индекса товара
from operator import index


def find_product(list, product):
    index_product = 0
    for _ in list:
        if _ == product:
            return index_product
        index_product += 1
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_product(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

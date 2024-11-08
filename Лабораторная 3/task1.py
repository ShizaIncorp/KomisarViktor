# TODO Напишите функцию для поиска индекса товара


def find_product(list, product):
    index_product = 0
    for i in list:
        if i == product:
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

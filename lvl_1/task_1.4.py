# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

sum_quant = 0 # общее количество товара
sum_price = 0 # общая стоимость товара
for name_of_product, code_product in titles.items(): # перебираем наименования и коды из словаря titles{}
    for list_of_dict in store[code_product]: # перебираем список словарей из словаря store{} для текущего товара с кодом code_product
        sum_quant = sum_quant + list_of_dict['quantity'] # подсчет количества товаров текущего наименования
        sum_price = sum_price + list_of_dict['price'] # подсчет общей суммы товаров текущего наименования
    print(f'{name_of_product} - {sum_quant} шт, стоимость {sum_price} руб')
    sum_quant = 0 # обнуляем количество для подсчета следующего товара
    sum_price = 0 # обнуляем общую стоимость подсчета следующего товара


    

# Python. Урок 2
# ВЫПОЛНЕНО - list и tuple
# ВЫПОЛНЕНО - условный оператор if
# ВЫПОЛНЕНО - операторы цикла for и while
# ВЫПОЛНЕНО - отладчик
# TODO - фибоначчи задача
# TODO - словари
# TODO - лаконичная запись циклов

# TODO - функции: параметры
# TODO - модули, пакеты, импорт


# # Типы данных
# x = 1  # числа
# word = 'Hello'  # строки

# # Изменяемый массив
# shop_list = ['Картошка', 'Капуста', 'Морковь']  # список




# Задача 1
# Приведем список покупок в магазине

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом

# # Узнаем список методов
# from pprint import pprint
# pprint(dir(shop_list))
print('пункт а')
print('Список до:', shop_list)

shop_list.insert(shop_list.index('Рис'), 'Рыба')

print('Список после:', shop_list)

#   b. Добавьте фрукты из списка fruits в конец списка shop_list

fruits = ['Яблоко', 'Апельсин', 'Клубника']

# shop_list.append(fruits)
# print(len(shop_list))  # ['Картофель', 'Горошек', 'Рыба', 'Рис', 'Хлеб', ['Яблоко', 'Апельсин', 'Клубника']]

shop_list.extend(fruits)
print('пункт b', shop_list, len(shop_list))

#   c. Удалите из списка shop_list картофель

# print(shop_list.pop(0))
# print(shop_list)

shop_list.remove('Картофель')
print('пункт c', shop_list, len(shop_list))  # ['Горошек', 'Рыба', 'Рис', 'Хлеб', 'Яблоко', 'Апельсин', 'Клубника']

#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 

# Формирование строк в Python
search = 'Хлеб'
# Вариант 1 - Передавать в качестве параметров списка
print('Номер', search, 'в списке -', shop_list.index(search) + 1)

print('Номер ' + search + ' в списке - ' + str(shop_list.index(search) + 1))

# Вариант 2 - форматирование строки
print('Номер {} в списке - {}'.format(search, shop_list.index(search) + 1))
# Проблема!
# url = 'https://www.ranepa.ru/my_profile/functions={}/{}/{}/{}'.format(????)

# Вариант 3 - f-строки
print(f'Номер {search} в списке - {shop_list.index(search) + 1}')



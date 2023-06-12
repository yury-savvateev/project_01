# Операторы цикла for, while

# Оператор while

# i = 1

# while i < 10:
#     i += 1  # i = i + 1
#     print('i =', i)

# print('До свидания')


# Сравнение цен на квартиры
# цикл можно использовать для перебора элементов списка
print('Здравствуйте!')
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
i = -1

while i < len(room_prices):
    i += 1
    price = room_prices[i]
    print('Проверяем ', price)

    if price == min(room_prices):
        print('Найдена минимальная цена')
        break

# print('До свидания!')

# # где увидеть оператор pass

# def func():
#     pass

# class Class:
#     pass

# i = -1
# word = 'Hello12'
# while i < len(word):
#     i += 1
#     if word[i].isdigit() == True:
#         print('Буква')
#     else:
#         pass



# Оператор цикла for
# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]

# for i in room_prices:
#     print('Цена команты =', i)


# разница между for и while
# через while
rainbow = ['red', 'green', 'blue', 'violet']
i = 0

while i < len(rainbow):
    print(rainbow[i])
    i += 1

# через for
for elem in rainbow:
    print(elem)

# перебрать индексы через for
for ind in range(len(rainbow)):
    print(rainbow[ind])

# получить пары (индекс, значение) с помощью enumerate()
# x, y = 1, 2
for ind, elem in enumerate(rainbow):
    print(f'Элемент {elem} - индекс {ind}')

""" """ # Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
    # 
    

month_list = [
    ['Январь', 31],
    ['Февраль', 28],
    ['Март', 31],
    ['Апрель', 30],
    ['Май', 31],
    ['Июнь', 30],
    ['Июль', 31],
    ['Август', 31],
    ['Сентябрь', 30],
    ['Октябрь', 31],
    ['Ноябрь', 30],
    ['Декабрь', 31]
]
month_number_input = input("Введите номер месяца (от 1 до 12): ")
if month_number_input.isdigit():
    month_number = int(month_number_input)
    if month_number < 1 or month_number > 12: 
        print("Такого месяца нет!")
    else:
            name_month = month_list[month_number - 1][0]
            days_quantity = month_list[month_number - 1][1]
            print(f'Вы ввели {name_month}. {days_quantity} дней')

else:
    print("Такого месяца нет!")


# Решение с применением кортежей

month_tuple = (
    ('Январь', 31),
    ('Февраль', 28),
    ('Март', 31),
    ('Апрель', 30),
    ('Май', 31),
    ('Июнь', 30),
    ('Июль', 31),
    ('Август', 31),
    ('Сентябрь', 30),
    ('Октябрь', 31),
    ('Ноябрь', 30),
    ('Декабрь', 31)
)

month_number_input = input("Введите номер месяца (от 1 до 12): ")
if month_number_input.isdigit() and int(month_number_input) > 0:
    month_number = int(month_number_input)
    if month_number < 1 or month_number > 12:
        print("Такого месяца нет!")
    else:
        name_month = month_tuple[month_number - 1][0]
        days_quantity = month_tuple[month_number - 1][1]
        print(f'Вы ввели {name_month}. {days_quantity} дней')
else:
    print("Такого месяца нет!")



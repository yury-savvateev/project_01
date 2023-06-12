# Python. Урок 3
# ВЫПОЛНЕНО - функции, параметры
# TODO - модули, пакеты, импорт

# Функция - вызываемый блок кода
# DRY - Dont repeat yourself 

# Этап создания функции
# # параметры - то что передается внутрь функции для обработки
# def greeting(name):
#     print('Hello', name)


# # Этап вызова функции
# for i in ['Марк', 'Филипп', 'Семен']:
#     greeting(i)



# Задача 3.1.
# Переоформить в виде функции

employees1 = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

employees2 = {'Ted' : 50000,
    'Kirill' : 150000,
    'Mike' : 130000,
    'Maria' : 100000,
    'Eve' : 81000}


# этап создания функции
# Аннотация к функции
def get_top_mgrs(empl: dict) -> list:
    '''
    Функция принимает словарь сотрудников 
    и возвращает список сотрудников, 
    у которых ЗП выше 10к в год.
    '''

    top_managers = []

    for name in empl:
        if empl[name] >= 100000:
            top_managers.append(name)

    # необходимо вернуть результат функции
    return top_managers



# Этап вызова функции
# for i in get_top_mgrs(employees2):
#     print(i)


# # Воспользуемся результатом этой функции
# total_sum = sum([employees1[n] for n in get_top_mgrs(employees1)])
# print(total_sum)


# Параметры функции
#   именнованные и позиционные параметры
#   параметры по умолчанию
#   распаковка параметров (или как работает функции print())

def trapezoid_s(h, *, a, b):
    '''Площадь трапеции'''
    return (a + b) / 2 * h

# вызов с позиционными параметрами
# St = trapezoid_s(5, 6, 10)
# print(St)

# # вызов с именованными параметрами
# St = trapezoid_s(a=5, h=10, b=6)
# print(St)

# комбинированный вызов
St = trapezoid_s(10, a=5, b=6)
print(St)


# Параметры по-умолчанию
def trapezoid_v(a, b, *, h=1):
    '''
    h - высота цилиндрической трапеции
    A, B - площади оснований цилиндрической трапеции
    '''
    return (1/3) * h * (a + b + (a * b)**.5)

Vt = trapezoid_v(5, 6)
print(Vt)


# как работает функции print()
print(1, 2, 'Hello', [1, 2], {'a': 1})

# запаковка параметров функции
def func(*args, **kwargs):
    print('Содержание args:', type(args))
    for i in args:
        print('    ', i)
         
    print('Содержание kwargs:', type(kwargs))
    for i in kwargs:
        print('    ', i, kwargs[i])


func(1, 2, 'Hello', [1, 2], {'a': 1}, a=5, b=4, word='HI')

# Кстати
# У функции print есть именованные параметры

print(1, 2, 3, sep='\n', end='\nevewcvewcvewc')

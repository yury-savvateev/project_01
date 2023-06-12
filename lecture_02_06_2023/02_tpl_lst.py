# Кортежи и списки

# Списки - изменяемые массивы
primes = [2, 3, 5, 7, 11, 13]
rainbow = ['red', 'green', 'blue']
mess_lst = ['red', 62, 2.3]
empty_lst = []

population = [
    ['Москва', 100000], 
    ['Нижний Новгород', 40000]
    ]

# Индексация списка внутри списка
# print(population[0][0], population[0][1])


# Кортеж - неизменяемый массив
archive = (1, 2, 3)
archive

# Отличие списков и кортежей
# Копирование списков
rainbow = ['red', 'green', 'blue']
colors = rainbow

colors.append('violet')

print(colors)

print(rainbow)

print(id(rainbow) == id(colors))
# Следовательно, присвоением список не копируется, а только лишь добавляется новый ярылык

# Копирование кортежа
archive = (1, 2, 3)
new_archive = archive

new_archive = new_archive + (4, 5)

print(archive, new_archive)
print(id(archive) == id(new_archive))
# Следовательно, при присвоение нового имени переменной создается новый объект в памяти

# Неизменяемые объекты:
# int, str, tuple и тд

# Изменяемые объекты:
# list, dict

# Где видим кортежи?
x, y, z = 1, 2, 3
(x, y, z) = (1, 2, 3)

def func(x, y):
    return y, x

var1, var2 = func(1, 2)  # вернется кортеж


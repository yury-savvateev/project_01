# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(list_of_analyses):
    i = 0
    min_number = list_of_analyses[0]
    while i < len(list_of_analyses) - 1:
        next_number = list_of_analyses[i+1]
        if next_number < min_number:
            min_number = next_number
        i = i + 1
    return min_number

def maximum(list_of_analyses):
    i = 0
    max_number = list_of_analyses[0]
    while i < len(list_of_analyses) - 1:
        next_number = list_of_analyses[i+1]
        if next_number > max_number:
            max_number = next_number
        i = i + 1
    return max_number

list_of_integers = [4,6,2,1,9,63,-134,566]
print(f'min = {minimum(list_of_integers)}, max = {maximum(list_of_integers)}')


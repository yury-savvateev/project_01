# main.py - служит файлом для запуска

# импорт имен из других модулей
# Вариант импорта 1
import functions

# Вариант импорта 2
# import functions as f

# for i in ['Марк', 'Филипп', 'Семен']:
#     print(f.func(i))
#     print(f.var1)

# Вариант импорта 3
# from functions import func
# from pprint import pprint

# for i in ['Марк', 'Филипп', 'Семен']:
#     print(func(i))

print(functions.__name__)
print(__name__) # __main__ - если файл является запускаемым, то его имя становится __main__

if __name__ == '__main__':
    print('Запуск скрипта!')
    
# Условный оператор

x = 0

# Язык динамической типизации
# x = 'a'

# Условие if
if x > 0:
    print('Больше нуля')
elif x < 0:
    print('Меньше нуля')
else:
    print('Равен нулю')

# Двоеточие означает отступ после переноса строки
# по PEP8



x, y = True, False
# Старшинство логических операторов
if y and not x or x:
    print('Истина')
else:
    print('Ложь')


# эластичность спроса по цене
elasticity_dem = 1
if elasticity_dem == 0:
    print('Товары первой необходимости')
    result = 0.0
elif 0 < elasticity_dem < 1:
    print('Нормальные блага')
    result = 0.5
elif elasticity_dem > 1:
    print('Роскошь')
    result = 3.0
else:
    print ('Товары низкого качества')
    result = -1.0
    if elasticity_dem == 1:
        print ('Единичная эластичность')
        result = 1.0
print('значение =',result)



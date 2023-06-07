# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_track_for_out = [] # создадим пустой список для проверки уникальности трека
len_time_of_track = 0
i = 1
while i <= 3: # посчитаем длительность 3 треков в цикле
    random_track = random.choice(my_favorite_songs)
    
    if not random_track in random_track_for_out: # проверим уникальность трека
        random_track_for_out.append(random_track) # добавим уникальный трэк в список для дальнейшей проверки уникальности
        len_time_of_track = len_time_of_track + random_track[1] # посчитаем длительность треков
        i = i + 1
        #print(random_track[0])

    
len_time_of_track = round(len_time_of_track, 2) # округлим длительность до 2 знака после запятой
print(f'Три песни звучат {len_time_of_track} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
my_favorite_songs_list = list(my_favorite_songs_dict.keys()) # поскольку словари не упорядочены, ключи словаря запишем в список
random_track_for_out = [] # создадим пустой список для проверки уникальности трека
len_time_of_track = 0 # начальное значение общей длительности 3 треков
i = 1
while i <= 3: # посчитаем длительность 3 треков в цикле
    random_key_dict = random.choice(my_favorite_songs_list) # сгенерим случайное значение из списка, оно же будет ключом в словаре (название трека)

    if not random_key_dict in random_track_for_out: # проверим уникальность трека
        random_track_for_out.append(random_track) # добавим уникальный трэк в список для дальнейшей проверки уникальности
        len_time_of_track = len_time_of_track + random_track[1] # посчитаем длительность треков
        i = i + 1
        #value_from_dict = my_favorite_songs_dict[random_key_dict]
        #print(random_key_dict, ' ', value_from_dict)

len_time_of_track = round(len_time_of_track, 2)
print(f'Три песни звучат {len_time_of_track} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

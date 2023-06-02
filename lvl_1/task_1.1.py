# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


# the first track
track_name = my_favorite_songs[:my_favorite_songs.find(',')]
print(track_name)

# the last track
track_name = my_favorite_songs[my_favorite_songs.rfind(',') + 2:]
print(track_name)

# the second track
number_start_character = my_favorite_songs.find(',') + 2
number_end_character = my_favorite_songs.find(',', number_start_character)
track_name = my_favorite_songs[number_start_character:number_end_character]
print(track_name)

# track the second from the end
my_favorite_songs_backwards = my_favorite_songs[::-1]
number_start_character = my_favorite_songs_backwards.find(',') + 1
number_end_character = my_favorite_songs_backwards.find(',',number_start_character) - 1
track_name = my_favorite_songs_backwards[number_start_character:number_end_character]
track_name = track_name[::-1]
print(track_name)
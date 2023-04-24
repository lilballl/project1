# Задача 1.1.

# Есть строка с перечислением песен

# my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print(len('Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'))
print(len('Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up,'))
print(len('Waste a Moment, Staying\' Alive, A Sorta Fairytale,'))
print(len("Waste a Moment, Staying\' Alive"))
print(len('Waste a Moment,'))
print(my_favorite_songs[:14],my_favorite_songs[63:],my_favorite_songs[15:30],my_favorite_songs[50:62])

# Данную задачу можно решить попроще
# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])

#Задача 1.2.

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
random_songs = random.sample(my_favorite_songs,3)
total_duration = random_songs[0][1] + random_songs[1][1] + random_songs[2][1]
print("Три песни звучат", total_duration, "минут")



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

from random import sample
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
data = list(my_favorite_songs_dict.items())
random_songs = sample(data,3)
total_duration = random_songs[0][1] + random_songs[1][1] + random_songs[2][1]
print("Три песни звучат", total_duration, "минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

# Отлично!

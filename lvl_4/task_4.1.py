# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('lvl_4/teatchers.db')
cursor = conn.cursor()

# Функция для получения информации о студенте и его школе по ID
def get_student_info(student_id):
    # Выполнение SQL-запроса
    cursor.execute('''SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, 
    School.School_Name FROM Students INNER JOIN School ON Students.School_Id = School.School_Id 
    WHERE Students.Student_Id = ?''', (student_id,))

    """ Пояснения к запросу:
    1. SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, Schools.School_Name - Это список столбцов, 
    которые мы хотим выбрать из таблицы. 
    Мы выбираем столбцы "Student_Id", "Student_Name", "School_Id" из таблицы "Students" 
    и столбец "School_Name" из таблицы "Schools".
    2. FROM Students - Это указывает, что мы выбираем данные из таблицы "Students".
    3. INNER JOIN Schools ON Students.School_Id = Schools.School_Id - Это оператор JOIN, который объединяет таблицу 
    "Students" с таблицей "Schools" по условию, что значения столбца "School_Id" в обеих таблицах совпадают.
    4. WHERE Students.Student_Id = ? - Это условие WHERE, которое фильтрует результаты запроса, 
    ограничивая только те строки, в которых значение столбца "Student_Id" равно определенному значению. 
    Знак "?" является параметром, который будет заменен фактическим значением во время выполнения запроса.
    5. (student_id,) - Это кортеж значений параметров запроса. Запятая в скобках обязательна и указывает на то, 
    что это кортеж  """
    
    result = cursor.fetchone() # Извлечение результатов запроса и запись в переменную result

    if result is not None: # Проверка есть ли результат запроса
        student_id, student_name, school_id, school_name = result
        # Вывод информации
        print("ID студента:", student_id)
        print("Имя студента:", student_name)
        print("ID школы:", school_id)
        print("Название школы:", school_name)
    else:
        print("Студент с указанным ID не найден.")

# Вызов функции для получения информации о студенте
get_student_info(201) #в данном случае ищем Ивана)


conn.close() # Закрытие соединения с базой данных

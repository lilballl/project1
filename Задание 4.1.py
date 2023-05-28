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

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE Students (
Student_Id  INTEGER NOT NULL,  
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY
);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id) 
VALUES 
(201, 'Иван', 1),
(202, 'Петр', 2),
(203, 'Анастасия', 3),
(204, 'Игорь', 4);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3


def get_student(student_id):
  connection = sqlite3.connect('teachers.db')
  cursor = connection.cursor()
  query = "SELECT FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_Id = ?"
  cursor.execute(query,(student_id)) 
    result = cursor.fetchone()
    if result:
        print('ID Студента:', result[0])
        print('Имя студента:', result[1])
        print('ID школы:', result[2])
        print('Название школы:', result[3])
    else:
        print('Студент с таким ID не найден')
connection.commit()
connection.close()

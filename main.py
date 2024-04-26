# Промежуточная контрольная работа по блоку Специализация.
#
# Необходимо написать проект, содержащий функционал работы с заметками.
# Выбор структуры для хранения (датафрейм Pandas) обуславливается простотой работы
# с файлами .csv, а также небольшими требованиями к объему массива заметок (объем
# заметок, как правило, не предполагает задействования значительного объема памяти
# и сложной организации хранения данных).

import os.path
import pandas as pd
import datetime


def note_books_print(books):
    print(books.to_string(index=False))


def print_help():
    print(*["add - добавить заметку",
            "save - записать книгу заметок в файл",
            "delete - удалить заметку",
            "help - помощь (список команд)",
            "edit - редактирование заметки",
            "print - печать списка заметок",
            "q - выход из программы без сохранения книги заметок в файл"], sep="\n")


if os.path.isfile('note_test.csv'):
    note_books_data = pd.read_csv('note_test.csv', encoding='utf-8', sep=';')
    identifikator_value = note_books_data['ИДЕНТИФИКАТОР'][len(note_books_data) - 1] + 1
else:
    print("Файла книги заметок не существует. Вы с ней сейчас начинаете работать")
    identifikator_value = 1
    note_books_data = pd.DataFrame(columns=['ИДЕНТИФИКАТОР',
                                            'ЗАГОЛОВОК',
                                            'СОДЕРЖАНИЕ ЗАМЕТКИ',
                                            'ДАТА И ВРЕМЯ СОХРАНЕНИЯ'])

print_help()
while True:
    print("--------------------------------------------------------------------------")
    temp_command = input("Введите команду ")
    if temp_command == "add":
        heading = input("Введите заголовок новой заметки ")
        content = input("Введите тело заметки ")
        new_row = {'ИДЕНТИФИКАТОР': identifikator_value, 'ЗАГОЛОВОК': heading,
                   'СОДЕРЖАНИЕ ЗАМЕТКИ': content, 'ДАТА И ВРЕМЯ СОХРАНЕНИЯ': datetime.datetime.now()}
        note_books_data = note_books_data._append(new_row, ignore_index=True)
        identifikator_value = identifikator_value + 1
        print("Заметка добавлена в книгу")
    elif temp_command == "save":
        note_books_data.to_csv('note_test.csv', encoding='utf-8', sep=';', index=False)
        print("Запись прошла успешно")
    elif temp_command == "edit":
        id_note_edit = int(input("Введите идентификатор заметки, которую хотите редактировать "))
        heading_edit = input("Введите новый заголовок заметки ")
        content_edit = input("Введите новое содержание заметки ")
        index_names_edit = note_books_data[note_books_data['ИДЕНТИФИКАТОР'] == id_note_edit].index
        note_books_data.drop(index_names_edit, inplace=True)
        new_row_edit = {'ИДЕНТИФИКАТОР': id_note_edit, 'ЗАГОЛОВОК': heading_edit,
                   'СОДЕРЖАНИЕ ЗАМЕТКИ': content_edit, 'ДАТА И ВРЕМЯ СОХРАНЕНИЯ': datetime.datetime.now()}
        note_books_data = note_books_data._append(new_row_edit, ignore_index=True)
        note_books_data = note_books_data.sort_values('ИДЕНТИФИКАТОР')
    elif temp_command == "delete":
        id_note = int(input("Введите идентификатор заметки, которую хотите удалить "))
        index_names = note_books_data[note_books_data['ИДЕНТИФИКАТОР'] == id_note].index
        note_books_data.drop(index_names, inplace=True)
    elif temp_command == "help":
        print_help()
    elif temp_command == "print":
        note_books_print(note_books_data)
    elif temp_command == "q":
        break
    else:
        print("Пожалуйста, правильно введите команду. (help - помощь")

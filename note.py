import json
import os
from datetime import datetime

notes_file = 'notes.json'

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r', encoding='UTF-8') as f:
            notes = json.load(f)
    else:
        notes = {}
    return notes

def save_notes(notes):
    with open(notes_file, 'w', encoding='UTF-8') as f:
        json.dump(notes, f, ensure_ascii=False)

def add_note():
    notes = load_notes()
    note_id = input('Введите идентификатор заметки: ')
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {
        'id': note_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes[note_id] = note
    save_notes(notes)
    print('Заметка сохранена.')

def edit_note():
    notes = load_notes()
    note_id = input('Введите идентификатор заметки для редактирования: ')
    if note_id in notes:
        note = notes[note_id]
        print('Редактирование заметки', note['title'])
        title = input('Введите новый заголовок заметки (оставьте пустым для сохранения текущего): ')
        if title:
            note['title'] = title
        body = input('Введите новый текст заметки (оставьте пустым для сохранения текущего): ')
        if body:
            note['body'] = body
        note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        notes[note_id] = note
        save_notes(notes)
        print('Заметка обновлена.')
    else:
        print('Заметка с таким идентификатором не найдена.')

def delete_note():
    notes = load_notes()
    note_id = input('Введите идентификатор заметки для удаления: ')
    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print('Заметка удалена.')
    else:
        print('Заметка с таким идентификатором не найдена.')

def list_notes():
    notes = load_notes()
    for note_id, note in notes.items():
        print('-' * 40)
        print('Идентификатор:', note['id'])
        print('Заголовок:', note['title'])
        print('Дата/время:', note['timestamp'])
        print('Текст:', note['body'])
    if not notes:
        print('Заметок пока нет.')

def main():
    print('Добро пожаловать в приложение заметки.')
    while True:
        print('Выберите действие:')
        print('1. Добавить заметку')
        print('2. Редактировать заметку')
        print('3. Удалить заметку')
        print('4. Показать список заметок')
        print('5. Выйти')
        choice = input('Введите номер действия: ')
        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            list_notes()
        elif choice == '5':
            print('До свидания!')
            break
        else:
            print('Неверный номер действия. Попробуйте еще раз.')


print(main())
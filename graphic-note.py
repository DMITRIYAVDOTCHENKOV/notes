import os
from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.simpledialog import askstring

# from tkinter.messagebox import askstring
# from tkinter import askstring

# создаем главное окно
root = Tk()
root.title("Мои заметки")

# создаем поле для ввода текста
text_box = Text(root, height=20, width=50)
text_box.pack(pady=10)

# создаем список сохраненных заметок
notes_list = Listbox(root, height=10, width=50)
notes_list.pack(pady=10)


# функция сохранения заметки
def save_note():
    # получаем текст из поля ввода
    note_text = text_box.get("1.0", "end-1c")

    # если текст не пустой
    if note_text:
        # создаем директорию для заметок, если ее еще нет
        if not os.path.exists("примечания"):
            os.mkdir("примечания")

        # спрашиваем у пользователя название заметки
        note_name = simpledialog.askstring("Название заметки", "Введите название заметки:")

        # если пользователь ввел название
        if note_name:
            # спрашиваем у пользователя категорию заметки
            categories = os.listdir("примечания")
            if categories:
                default_category = categories[0]
            else:
                default_category = None
            category_name = askstring("Категория заметки", "Выберите категорию заметки:", initialvalue=default_category,
                                      parent=root)

            # создаем путь к файлу заметки
            if category_name:
                category_path = os.path.join("примечания", category_name)
                if not os.path.exists(category_path):
                    os.mkdir(category_path)

                note_filename = os.path.join(category_path, f"{note_name}.txt")

                # сохраняем заметку в файл
                with open(note_filename, "w") as f:
                    f.write(note_text)

                # очищаем поле ввода
                text_box.delete("1.0", "end")

                # добавляем название заметки в список сохраненных заметок
                notes_list.insert(END, note_name)


# функция загрузки заметки
def load_note():
    if notes_list.curselection():
    # получаем название выбранной заметки
        selected_note = notes_list.get(notes_list.curselection())

    # создаем путь к файлу заметки
    categories = os.listdir("примечания")
    for category in categories:
        category_path = os.path.join("примечания", category)
        if os.path.isdir(category_path):
            примечания = os.listdir(category_path)
            for note in примечания:
                if note.endswith(".txt") and note[:-4] == selected_note:
                    note_filename = os.path.join(category_path, note)
                    # загружаем текст заметки
                    with open(note_filename, "r") as f:
                        note_text = f.read()
                        text_box.delete("1.0", "end")
                        text_box.insert("1.0", note_text)

# функция удаления заметки
def delete_note():
    # получаем название выбранной заметки
    selected_note = notes_list.get(notes_list.curselection())

    # создаем путь к файлу заметки
    note_filename = os.path.join("notes", f"{selected_note}.txt")

    # удаляем файл заметки
    os.remove(note_filename)

    # удаляем название заметки из списка сохраненных заметок
    notes_list.delete(notes_list.curselection())


# добавляем кнопки для  сохранения, загрузки и удаления заметок
save_button = Button(root, text="Сохранить заметку", command=save_note)
save_button.pack(side=LEFT, padx=10)

load_button = Button(root, text="Загрузить заметку", command=load_note)
load_button.pack(side=LEFT, padx=10)

delete_button = Button(root, text="Удалить заметку", command=delete_note)
delete_button.pack(side=LEFT, padx=10)

# заполняем список сохраненных заметок
if os.path.exists("notes"):
    categories = os.listdir("notes")
    for category in categories:
        category_path = os.path.join("notes", category)
        if os.path.isdir(category_path):
            notes = os.listdir(category_path)
            for note in notes:
                if note.endswith(".txt"):
                    note_name = note[:-4]
                    notes_list.insert()

# запускаем главный цикл обработки событий
root.mainloop()

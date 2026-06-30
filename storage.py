import json
from models import Book

# В эту функцию мы подаем список из объектов (книг)
# тут мы их разбиваем на словари с помощью класс метода Book
# и загружаем в json формате в файл


def storage(books):
    try:
        with open("BooksData.json", "r", encoding="utf-8") as file:
            library =  json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Ловим отсутствие файла ИЛИ если файл пустой/поврежден
        library = []

    for book in books:
        library.append(book.to_dict())

    with open("BooksData.json", "w", encoding="utf-8") as file:
        json.dump(library, file, ensure_ascii=False, indent=4)

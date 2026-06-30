import json
from models import Book

# В эту функцию мы подаем список из объектов (книг)
# тут мы их разбиваем на словари с помощью класс метода Book
# и загружаем в json формате в файл


def storage(new_library):
    # Загружаем библиотеку книг из файла
    try:
        with open("BooksData.json", "r", encoding="utf-8") as file:
            library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Ловим отсутствие файла ИЛИ если файл пустой/поврежден
        library = []

    existing_books = set()  # хеш-таблица для быстрого поиска повторов

    for book in library:
        existing_books.add((book['title'].lower(), book['author'].lower()))

    # Обрабатываем список тех книг,
    # которые ввел пользователь во время работы приложения
    for book in new_library:
        book_dict = book.to_dict()
        new_title_lower = book_dict['title'].lower()
        new_author_lower = book_dict['author'].lower()

        # Получаем кортеж из названия книги и ее автора
        new_book_key = (new_title_lower, new_author_lower)

        # Проверяем, была ли эта в библиотеке книг
        if new_book_key in existing_books:
            print(f"Предупреждение: Книга '{book_dict['title']}' уже есть в базе! Дубликат пропущен!")
        else:
            library.append(book_dict)
            existing_books.add(new_book_key)

    with open("BooksData.json", "w", encoding="utf-8") as file:
        json.dump(library, file, ensure_ascii=False, indent=4)

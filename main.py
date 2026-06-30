import storage
import stats
from models import Book


def main():
    # 1. При СТАРТЕ программы один раз загружаем старые книги с диска через storage

    library = [Book.from_dict(item) for item in storage.storage([])]

    print("=== СИСТЕМА УЧЕТА КНИГ ===\n"
          "== Список команд ==:\n"
          "1. Добавить новую книгу\n"
          "2. Показать все книги\n"
          "3. Посмотреть статистику\n"
          "4. Выйти из программы")

    while True:
        try:
            choice = int(input("\nВыберите одно действие (число): ").strip())
        except Exception:
            print("Ошибка, попробуйте ввести число!")
            continue

        # КОМАНДА 1: ДОБАВЛЕНИЕ КНИГИ
        if choice == 1:
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            rating = input("Введите вашу оценку (1-5): ").strip()
            date = input("Введите дату прочтения: ").strip()

            # Создаем живой объект книги
            new_book = Book(title, author, rating, date)
            # Просто кладем его в наш рабочий список в памяти
            library.append(new_book)
            print(f"Книга '{title}' успешно добавлена в список!")

        # КОМАНДА 2: ПОКАЗ ВСЕХ КНИГ
        elif choice == 2:
            if not library:
                print("Ваша библиотека пока пуста.")
            else:
                print("\n--- СПИСОК ВАШИХ КНИГ ---")
                for index, book in enumerate(library, start=1):
                    # Используем встроенный метод __str__ нашего класса Book
                    print(f"{index}. {book}")

        # КОМАНДА 3: АНАЛИТИКА И СТАТИСТИКА
        elif choice == 3:
            if not library:
                print("Нет данных для подсчета статистики.")
            else:
                print("\n--- СТАТИСТИКА БИБЛИОТЕКИ ---")
                # Вызываем функции из нашего активированного модуля stats.py
                avg = stats.get_average_rating(library)
                authors = stats.get_author_stats(library)

                print(f"Средняя оценка ваших книг: {avg}")
                print("Количество книг по авторам:")
                for author, count in authors.items():
                    print(f" - {author}: {count} шт.")

        # КОМАНДА 4: ВЫХОД И СОХРАНЕНИЕ В JSON
        elif choice == 4:
            # Передаем весь наш список объектов в storage для разбора и записи в файл
            storage.storage(library)
            break

        else:
            print("Ошибка: Неверный ввод! Пожалуйста, выберите пункт от 1 до 4.")


if __name__ == "__main__":
    main()

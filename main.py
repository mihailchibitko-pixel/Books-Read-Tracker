def main():
    print("=== СИСТЕМА УЧЕТА КНИГ ===\n"
          "== Список команд ==:\n"
          "1. Добавить новую книгу\n"
          "2. Показать все книги\n"
          "3. Посмотреть статистику\n"
          "4. Выйти из программы")
    while True:
        try:
            choice = int(input("\nВыберите одно действие (число): ").strip())
        except Exception as er:
            print(f"Ошибка, попробуйте ввести число! {er}")
            continue

        if choice == "1":
            print("TODO: Здесь будет вызов функции добавления из storage.py")
        elif choice == "2":
            print("TODO: Здесь будет вызов функции чтения из storage.py")
        elif choice == "3":
            print("TODO: Здесь будет вызов аналитики из stats.py")
        elif choice == "4":
            print("Успешный выход из программы!")
            break
        else:
            print("Ошибка: Неверный ввод! Пожалуйста, выберите пункт от 1 до 4.")


if __name__ == "__main__":
    main()
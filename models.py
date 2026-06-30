class Book:
    def __init__(self, title, author, rating, date):
        self.title = title        # Название книги
        self.author = author      # Автор книги
        self.rating = rating      # Оценка книги
        self.date = date          # Дата прочтения

    def __str__(self):
        """Красивый вывод книги при печати"""
        return f"'{self.title}' — {self.author} (Оценка: {self.rating}, Дата: {self.date})"

    # Метод разбора объекта в простой словарь для JSON-формата
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
            "date": self.date
        }

    # Метод сборки объекта Book из словаря, прочитанного из файла
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            rating=data["rating"],
            date=data["date"]
        )

class Book:
    def __init__(self, title, author, rating, date):
        self.title = title
        self.author = author
        self.rating = rating
        self.date = date

    def __str__(self):
        return f"'{self.title}' — {self.author} (Оценка: {self.rating}, Дата: {self.date})"

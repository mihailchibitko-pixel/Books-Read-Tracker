def get_average_rating(books):
    """Подсчёт средней оценки всех книг в списке"""
    if not books:
        return 0.0
    # На всякий случай переводим rating в float, так как из JSON он может прийти строкой
    total = sum(float(book.rating) for book in books)
    return round(total / len(books), 2)

def get_author_stats(books):
    """Статистика: сколько книг написал каждый автор"""
    stats = {}
    for book in books:
        stats[book.author] = stats.get(book.author, 0) + 1
    return stats

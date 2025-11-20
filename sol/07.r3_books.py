class Book:
    def __init__(self, name: str, author: str) -> None:
        self.name = name
        self.author = author


class Bookshelf:
    def __init__(self, books: list[Book]) -> None:
        self._books = books

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def group_by_author(self) -> dict[str, list[Book]]:
        result: dict[str, list[Book]] = {}
        for book in self._books:
            if book.author not in result:
                result[book.author] = []
            result[book.author].append(book)
        return result

    def books(self) -> list[Book]:
        return self._books

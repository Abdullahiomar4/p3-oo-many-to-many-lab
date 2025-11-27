# many_to_many.py

class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self)

    def __repr__(self):
        return f"<Book: {self.title}>"

    # Return all contracts for this book
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # Return all authors who have contracts for this book
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)

    def __repr__(self):
        return f"<Author: {self.name}>"

    # Return all contracts for this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # Return all books for this author
    def books(self):
        return [contract.book for contract in self.contracts()]

    # Create and return a new contract
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        return Contract(self, book, date, royalties)

    # Return total royalties for this author
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    # Tests expect this list name exactly:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    def __repr__(self):
        return f"<Contract: {self.author.name} - {self.book.title} ({self.date})>"

    @classmethod
    def contracts_by_date(cls, date):
        # Filter contracts by matching date
        filtered = [contract for contract in cls.all if contract.date == date]

        # Sort by author name then book title for consistent ordering
        return sorted(filtered, key=lambda c: (c.author.name, c.book.title))

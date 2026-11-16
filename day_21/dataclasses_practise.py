from dataclasses import dataclass

@dataclass
class Book:
    title: str
    pages: int = 0
    
    def describe(self):
        return f'{self.title} has {self.pages} pages.'

book = Book('Python Basics')
print(book)
print(book.pages)
print(book.title)
print(book.describe())


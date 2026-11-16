class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def describe(self):
        return f'{self.title} has {self.pages} pages.'


book1 = Book('Python Basics', 200)
print(book1.describe())
book2 = Book('HTML for everyone', 100)
print(book2.describe())
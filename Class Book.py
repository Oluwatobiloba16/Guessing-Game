class Book:
    def _init_(self, title, author, pages):
        self._title = title  # Encapsulation: Using a protected attribute
        self._author = author
        self._pages = pages
    
    def display_info(self):
        return f"'{self._title}' by {self._author}, {self._pages} pages"
    
    def read(self):
        return f"You start reading '{self._title}'."
    
    def bookmark_page(self, page):
        if 1 <= page <= self._pages:
            return f"Bookmarked page {page} in '{self._title}'."
        else:
            return f"Invalid page number. The book has {self._pages} pages."
    
# Example usage
book1 = Book("1984", "George Orwell", 328)
print(book1.display_info())
print(book1.read())
print(book1.bookmark_page(150))
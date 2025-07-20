# Retrieve Operation

## Python Command Used:

```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")

# To show all attributes of all books:
all_books = Book.objects.all()
for book in all_books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
----------------------------------------------------------------------------------------------------------

# Expected Output (from shell):
----------------------------
>>> from bookshelf.models import Book
>>> retrieved_book = Book.objects.get(title="1984")
>>> retrieved_book.title
'1984'
>>> retrieved_book.author
'George Orwell'
>>> retrieved_book.publication_year
1949
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
...
Title: 1984, Author: George Orwell, Year: 1949
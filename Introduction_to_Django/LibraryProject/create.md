# Create Operation

## Python Command Used:

```python
from bookshelf.models import Book

book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
------------------------------------------------------------------------------------
# Expected Output (from shell):
--------
>>> from bookshelf.models import Book
>>> book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book1
<Book: 1984 by George Orwell (1949)>
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
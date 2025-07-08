# Delete Operation

## Python Command Used:

```python
from bookshelf.models import Book

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
--------------------------------------------------------------

# Expected Output (from shell):
--------------------------
>>> from bookshelf.models import Book
>>> book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
>>> book_to_delete.delete()
(1, {'bookshelf.Book': 1}) # Output indicating 1 book was deleted
>>> Book.objects.all()
<QuerySet []> # Confirming no books are left
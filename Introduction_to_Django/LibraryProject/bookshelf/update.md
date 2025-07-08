# Update Operation

## Python Command Used:

```python
from bookshelf.models import Book

book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
-------------------------------------------------------------------

# Expected Output (from shell):
-------------------------------
>>> from bookshelf.models import Book
>>> book_to_update = Book.objects.get(title="1984")
>>> book_to_update.title = "Nineteen Eighty-Four"
>>> book_to_update.save()
>>> Book.objects.get(id=book_to_update.id).title
'Nineteen Eighty-Four'
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
# Update Operation

## Python Command Used:

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
-------------------------------------------------------------------

# Expected Output (from shell):
-------------------------------
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.get(id=book.id).title
'Nineteen Eighty-Four'
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
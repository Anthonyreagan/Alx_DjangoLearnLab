from .models import Author, Book, Library, Librarian

# Query all books by a specific author

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

    # List all books in a library
def books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    return Library.objects.get(name=library_name).librarian

# advanced_features_and_security/LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date', 'genre']
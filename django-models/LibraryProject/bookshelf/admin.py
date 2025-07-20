# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Define the admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # Fields to display in the list view
    list_filter = ('publication_year', 'author',) # Fields to filter by
    search_fields = ('title', 'author',) # Fields to search by

# Register your model with the custom admin class
admin.site.register(Book, BookAdmin)
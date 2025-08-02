# bookshelf/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Import your model here
from .models import Book

# --- Function-Based Views (FBV) ---
# This approach uses the @permission_required decorator directly on a function.

# @permission_required decorator
# The first argument is the permission string (e.g., 'app_label.permission_codename').
# The 'raise_exception=True' argument tells Django to raise a 403 Forbidden error
# if the user is logged in but doesn't have the permission.
# If the user is not logged in, they will be redirected to the login page.

@permission_required('bookshelf.add_book', raise_exception=True)
def book_create_fbv(request):
    """
    Function-based view to create a new Book instance.
    Requires 'bookshelf.add_book' permission.
    """
    # This view would contain the logic for a form to create a new book.
    # We'll just provide a simple placeholder for now.
    if request.method == 'POST':
        # Process form data and save the book
        return redirect('book-list')
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.change_book', raise_exception=True)
def book_update_fbv(request, pk):
    """
    Function-based view to update an existing Book instance.
    Requires 'bookshelf.change_book' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Process form data and save the updated book
        return redirect('book-detail', pk=book.pk)
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.delete_book', raise_exception=True)
def book_delete_fbv(request, pk):
    """
    Function-based view to delete an existing Book instance.
    Requires 'bookshelf.delete_book' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# --- Class-Based Views (CBV) ---
# For CBVs, using the PermissionRequiredMixin is the recommended and cleaner approach.
# You simply set the 'permission_required' attribute on the class.

class BookListView(ListView):
    """
    Class-based view to list all books.
    This view does not require any special permissions to view.
    """
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    """
    Class-based view to display a single book's details.
    This view also does not require any special permissions.
    """
    model = Book
    template_name = 'bookshelf/book_detail.html'
    context_object_name = 'book'

class BookCreateView(PermissionRequiredMixin, CreateView):
    """
    Class-based view to create a new book.
    Inherits from PermissionRequiredMixin to enforce permissions.
    Requires 'bookshelf.add_book' permission.
    """
    model = Book
    fields = ['title', 'author', 'published_date'] # Example fields
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'bookshelf.add_book'

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Class-based view to update a book.
    Requires 'bookshelf.change_book' permission.
    """
    model = Book
    fields = ['title', 'author', 'published_date'] # Example fields
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'bookshelf.change_book'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class-based view to delete a book.
    Requires 'bookshelf.delete_book' permission.
    """
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'bookshelf.delete_book'

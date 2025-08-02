# bookshelf/urls.py

from django.urls import path

# Import all views from the bookshelf app
from .views import (
    book_create_fbv,
    book_update_fbv,
    book_delete_fbv,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # --- Function-Based View (FBV) URLs ---
    # These URLs are mapped to the function-based views.
    path('fbv/create/', book_create_fbv, name='book-create-fbv'),
    path('fbv/update/<int:pk>/', book_update_fbv, name='book-update-fbv'),
    path('fbv/delete/<int:pk>/', book_delete_fbv, name='book-delete-fbv'),

    # --- Class-Based View (CBV) URLs ---
    # These URLs are mapped to the class-based views.
    path('', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/edit/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

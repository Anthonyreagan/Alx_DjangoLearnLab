# api_project/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet # Import BookList if you're keeping it

# Create a router instance
router = DefaultRouter()

# Register your BookViewSet with the router
# The 'r' before 'books_all' indicates a raw string, often used for regex patterns
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView) - keeping it as per task
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
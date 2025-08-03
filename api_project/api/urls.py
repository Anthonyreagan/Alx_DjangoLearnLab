# api_project/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authtoken_views # Import this

from .views import BookList, BookViewSet # Import BookList if you're keeping it

router = DefaultRouter()

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),

    path('', include(router.urls)),  # This includes all routes registered with the router
    path('api-token-auth/', authtoken_views.obtain_auth_token, name='api_token_auth'),
]
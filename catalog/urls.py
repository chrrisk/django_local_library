# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /catalog/
    path('books/', views.BookListView.as_view(), name='books'),  # /catalog/books/
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # /catalog/book/1/
    path('authors/', views.AuthorListView.as_view(), name='authors'),  # /catalog/authors/
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),  # /catalog/author/1/
]


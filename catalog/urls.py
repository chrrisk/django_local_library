# catalog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /catalog/
    path('books/', views.BookListView.as_view(), name='books'),  # /catalog/books/
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # /catalog/book/1/
    path('authors/', views.AuthorListView.as_view(), name='authors'),  # /catalog/authors/
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),  # /catalog/author/1/
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# catalog/urls.py (append)
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]

from django.urls import path

from bookstore.views import list_books, book_description, infobook, infoauthor, create_book

urlpatterns = [
    path('', list_books, name='base'),
    path('create_book', create_book),
    path('<title>', book_description, name='book'),
    path('<title>/infobook', infobook),
    path('infoauthor/<int:index>', infoauthor),

]
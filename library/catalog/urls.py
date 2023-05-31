from django.urls import path, include
from . import views

urlpatterns = [
    path('', (views.MainListView.as_view()), name='main'),
    path('authors/', (views.AuthorListView.as_view()), name='authors'),
    path('clients/', (views.ClientListView.as_view()), name='clients'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('book/create/', (views.BookCreateView.as_view()), name='addBook'),
    path('book/<int:pk>', views.BookView, name='book'),
    path('book/<int:pk>/update', (views.BookUpdateView.as_view()), name='updateBook'),
    path('book/<int:pk>/delete', (views.BookDeleteView.as_view()), name='deleteBook'),
    path('book/<int:pk>/renew', views.renew_book, name='renewBook'),

    path('author/create/', (views.AuthorCreateView.as_view()), name='addAuthor'),
    path('author/<int:pk>', views.AuthorView, name='author'),
    path('author/<int:pk>/update', (views.AuthorUpdateView.as_view()), name='updateAuthor'),
    path('author/<int:pk>/delete', (views.AuthorDeleteView.as_view()), name='deleteAuthor'),

    path('client/create/', (views.ClientCreateView.as_view()), name='addClient'),
    path('client/<int:pk>', views.ClientView, name='client'),
    path('client/<int:pk>/update', (views.ClientUpdateView.as_view()), name='updateClient'),
    path('client/<int:pk>/delete', (views.ClientDeleteView.as_view()), name='deleteClient'),

]

import django.shortcuts
from django.shortcuts import render
from django.views import View

from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *


class MainListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'catalog/main.html',
                      {'books': books})


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'catalog/authors_list.html',
                      {'authors': authors})


class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'catalog/clients_list.html',
                      {'clients': clients})


def BookView(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'catalog/book.html', {'book': book})


def AuthorView(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, 'catalog/author.html', {'author': author})


def ClientView(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, 'catalog/client.html', {'client': client})


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'genre', 'image']
    success_url = '/'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'genre', 'image']
    success_url = '/'


def renew_book(request, pk):
    book = django.shortcuts.get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book.return_date = form.cleaned_data['return_date']
            book.ClientView = form.cleaned_data['client']
            book.on_loan = True
    else:
        form = RenewBookForm(initial={'return_date': datetime.date.today() + datetime.timedelta(weeks=3)})
    return render(request, 'catalog/book_renew.html', {'form': form, 'book': book})


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'


class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/authors/'


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = '/clients/'


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = '/clients/'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/clients/'

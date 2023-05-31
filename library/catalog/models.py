from django.db import models
from django.urls import reverse


class Genre(models.Model):
    genreName = models.CharField(max_length=30)

    def __str__(self):
        return self.genreName

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['genreName']


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия автора')

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name','first_name']


class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия клиента')

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['last_name', 'first_name']


class Book(models.Model):
    title = models.CharField('Название книги', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Автор книги')
    summary = models.TextField('Краткое описание', max_length=1000, default='', blank=True)
    genre = models.ManyToManyField(Genre, blank=True, verbose_name='Жанры книги')
    image = models.ImageField(default='img/books/default.webp', upload_to='img/books', blank=True,
                              verbose_name='Фотография книги')
    return_date = models.DateField('Дата возвращения книги', blank=True, null=True)
    on_loan = models.BooleanField('Во временное пользование', null=True, default=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Клиент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': str(self.id)})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']






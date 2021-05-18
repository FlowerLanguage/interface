from django.shortcuts import render
from father import view
from book.models import Book
from book.serializers import BookSerializer


# Create your views here.
class BookListView(view.ListView):
    def __init__(self):
        super(BookListView, self).__init__(Book.objects.all(), BookSerializer, ['id', 'title', 'author'])


class BookDetailView(view.DetailView):
    def __init__(self):
        super(BookDetailView, self).__init__(Book.objects.all(), BookSerializer)

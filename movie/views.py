from django.shortcuts import render
from movie.models import Movie2011
from movie.serializers import Movie2011Serializer
from father import view


# Create your views here.
class Movie2011ListView(view.ListView):
    def __init__(self):
        super().__init__(Movie2011.objects.all(), Movie2011Serializer, ['id', 'name', 'box'])


class Movie2011DetailView(view.DetailView):
    def __init__(self):
        super().__init__(Movie2011.objects.all(), Movie2011Serializer)

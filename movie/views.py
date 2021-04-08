from django.shortcuts import render
from movie import models
from movie import serializers
from father import view

# Create your views here.
filter_fields = ['id', 'name', 'box']  # 设定下面所有list的过滤字段


# list
class MovieWholeListView(view.ListView):
    def __init__(self):
        super().__init__(models.MovieWhole.objects.all(), serializers.MovieWholeSerializer, filter_fields)


class Movie2021ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2021.objects.all(), serializers.Movie2021Serializer, filter_fields)


class Movie2020ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2020.objects.all(), serializers.Movie2020Serializer, filter_fields)


class Movie2019ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2019.objects.all(), serializers.Movie2019Serializer, filter_fields)


class Movie2018ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2018.objects.all(), serializers.Movie2018Serializer, filter_fields)


class Movie2017ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2017.objects.all(), serializers.Movie2017Serializer, filter_fields)


class Movie2016ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2016.objects.all(), serializers.Movie2016Serializer, filter_fields)


class Movie2015ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2015.objects.all(), serializers.Movie2015Serializer, filter_fields)


class Movie2014ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2014.objects.all(), serializers.Movie2014Serializer, filter_fields)


class Movie2013ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2013.objects.all(), serializers.Movie2013Serializer, filter_fields)


class Movie2012ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2012.objects.all(), serializers.Movie2012Serializer, filter_fields)


class Movie2011ListView(view.ListView):
    def __init__(self):
        super().__init__(models.Movie2011.objects.all(), serializers.Movie2011Serializer, filter_fields)


# detail
class MovieWholeDetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.MovieWhole.objects.all(), serializers.MovieWholeSerializer)


class Movie2021DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2021.objects.all(), serializers.Movie2021Serializer)


class Movie2020DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2020.objects.all(), serializers.Movie2020Serializer)


class Movie2019DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2019.objects.all(), serializers.Movie2019Serializer)


class Movie2018DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2018.objects.all(), serializers.Movie2018Serializer)


class Movie2017DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2017.objects.all(), serializers.Movie2017Serializer)


class Movie2016DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2016.objects.all(), serializers.Movie2016Serializer)


class Movie2015DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2015.objects.all(), serializers.Movie2015Serializer)


class Movie2014DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2014.objects.all(), serializers.Movie2014Serializer)


class Movie2013DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2013.objects.all(), serializers.Movie2013Serializer)


class Movie2012DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2012.objects.all(), serializers.Movie2012Serializer)


class Movie2011DetailView(view.DetailView):
    def __init__(self):
        super().__init__(models.Movie2011.objects.all(), serializers.Movie2011Serializer)

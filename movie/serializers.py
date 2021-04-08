from rest_framework.serializers import ModelSerializer
from movie import models


class MovieWholeSerializer(ModelSerializer):
    class Meta:
        model = models.MovieWhole
        fields = '__all__'


class Movie2021Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2021
        fields = '__all__'


class Movie2020Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2020
        fields = '__all__'


class Movie2019Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2019
        fields = '__all__'


class Movie2018Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2018
        fields = '__all__'


class Movie2017Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2017
        fields = '__all__'


class Movie2016Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2016
        fields = '__all__'


class Movie2015Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2015
        fields = '__all__'


class Movie2014Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2014
        fields = '__all__'


class Movie2013Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2013
        fields = '__all__'


class Movie2012Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2012
        fields = '__all__'


class Movie2011Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2011
        fields = '__all__'

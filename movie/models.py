from django.db import models


# Create your models here.
class Movie(models.Model):  # 模板类,后面所有电影类与他继承
    name = models.CharField(max_length=20)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房
    avg_avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页


class MovieWhole(Movie):
    class Meta:
        db_table = 'movie_whole'


class Movie2021(Movie):
    class Meta:
        db_table = 'movie_2021'


class Movie2020(Movie):
    class Meta:
        db_table = 'movie_2020'


class Movie2019(Movie):
    class Meta:
        db_table = 'movie_2019'


class Movie2018(Movie):
    class Meta:
        db_table = 'movie_2018'


class Movie2017(Movie):
    class Meta:
        db_table = 'movie_2017'


class Movie2016(Movie):
    class Meta:
        db_table = 'movie_2016'


class Movie2015(Movie):
    class Meta:
        db_table = 'movie_2015'


class Movie2014(Movie):
    class Meta:
        db_table = 'movie_2014'


class Movie2013(Movie):
    class Meta:
        db_table = 'movie_2013'


class Movie2012(Movie):
    class Meta:
        db_table = 'movie_2012'


class Movie2011(Movie):
    class Meta:
        db_table = 'movie_2011'

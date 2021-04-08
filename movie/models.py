from django.db import models


# Create your models here.

class MovieWhole(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_whole'


class Movie2021(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2021'


class Movie2020(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2020'


class Movie2019(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2019'


class Movie2018(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2018'


class Movie2017(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2017'


class Movie2016(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2016'


class Movie2015(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2015'


class Movie2014(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2014'


class Movie2013(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2013'


class Movie2012(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2012'


class Movie2011(models.Model):
    name = models.CharField(max_length=50)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)
    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)
    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie_2011'

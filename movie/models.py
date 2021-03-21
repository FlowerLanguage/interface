from django.db import models


# Create your models here.
class Movie2011(models.Model):
    name = models.CharField(max_length=20)  # 电影名
    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房
    avg_avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价
    avg_players = models.DecimalField(max_length=5, decimal_places=0)  # 场均人次
    url = models.URLField()  # 电影详情页

    class Meta:
        db_table = 'movie2011'

from django.db import models


# Create your models here.
class HousePrice(models.Model):
    city = models.CharField(max_length=20)  # 城市名
    avg_unit_price = models.DecimalField(decimal_places=2, max_digits=10)  # 平均单价
    chain_comparison = models.CharField(max_length=20)  # 环比
    year_on_year = models.CharField(max_length=20)  # 同比

    class Meta:
        db_table = 'house_price_202102'


class HousePrice202104(models.Model):
    city = models.CharField(max_length=20)  # 城市名
    avg_unit_price = models.DecimalField(decimal_places=2, max_digits=10)  # 平均单价
    chain_comparison = models.CharField(max_length=20)  # 环比
    year_on_year = models.CharField(max_length=20)  # 同比

    class Meta:
        db_table = 'house_price_202104'

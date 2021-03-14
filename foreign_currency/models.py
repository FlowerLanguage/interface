from django.db import models


# Create your models here.
class ForeignCurrency(models.Model):
    date = models.DateField(default='2000-1-1',max_length=20)  # 日期
    close = models.DecimalField(max_digits=10, decimal_places=4)  # 收盘
    open = models.DecimalField(max_digits=10, decimal_places=4)  # 开盘
    high = models.DecimalField(max_digits=10, decimal_places=4)  # 高
    low = models.DecimalField(max_digits=10, decimal_places=4)  # 低
    net_chg_pct = models.DecimalField(max_digits=10, decimal_places=4)  # 涨跌幅
    symbol = models.CharField(max_length=20)  # 期货类型

    class Meta:
        db_table = 'foreign_currency'  # 外汇数据表名

from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, default=None)  # 标题
    cover = models.URLField(default='https://www.dushu.com/book/1175_1.html')  # 封面
    author = models.CharField(max_length=100, default=None)  # 作者
    publisher = models.CharField(max_length=100, default=None)  # 出版商
    isbn = models.CharField(max_length=100, default=None)  # ISBN
    time = models.DateField(default='2021-05-18', max_length=20)  # 时间
    pack = models.CharField(max_length=100, default=None)  # 包装
    url = models.URLField(default='https://www.dushu.com/book/13802642/')  # 详情地址

    class Meta:
        db_table = 'book'  # 文学书籍表名

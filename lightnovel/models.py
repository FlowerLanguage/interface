from django.db import models


# Create your models here.
class HotNovel(models.Model):
    title = models.CharField(max_length=100, default=None)  # 标题
    classification = models.CharField(max_length=100, default=None)  # 文库分类
    author = models.CharField(max_length=100, default=None)  # 作者
    status = models.CharField(max_length=100, default=None)  # 小说状态
    update = models.DateField(default=None)  # 最后更新
    length = models.IntegerField(default=0)  # 文章长度
    cover = models.URLField(default='http://www.wenku8.net/index.php')  # 小说封面

    class Meta:
        db_table = 'hot_novel'  # 存储的数据表名


class UserOperation(models.Model):
    username = models.CharField(max_length=50, default=None)  # 用户id
    novel_id = models.IntegerField(default=None)  # 小说序号
    read = models.IntegerField(default=0, null=True)  # 阅读次数
    STATUS_CHOICES = (
        (1, '收藏'),
        (0, '没有收藏'),
    )
    collection = models.IntegerField(default=0, choices=STATUS_CHOICES, null=True)  # 是否收藏
    comment = models.CharField(max_length=10000, default=None, null=True)  # 评论
    download = models.IntegerField(default=0, null=True)  # 下载次数

    class Meta:
        db_table = 'user_operation'

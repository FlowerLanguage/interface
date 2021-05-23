from django.db import models


# Create your models here.
class MOVIES(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'MOVIES'  # 影视数据表名


class ENTERTAINMENT(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'ENTERTAINMENT'  # 娱乐数据表名


class ZOO(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'ZOO'  # 动物圈数据表名


class FOOD(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'FOOD'  # 美食数据表名


class LIFE(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'LIFE'  # 生活数据表名


class CAR(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'CAR'  # 汽车数据表名


class DIGITAL(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'DIGITAL'  # 数码数据表名


class KNOWLEDGE(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'KNOWLEDGE'  # 知识数据表名


class GAME(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'GAME'  # 游戏数据表名


class DANCE(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'DANCE'  # 舞蹈数据表名


class MUSIC(models.Model):
    title = models.CharField(max_length=100, default=None)  # 视频标题
    author = models.CharField(max_length=100, default=None)  # 视频作者
    pubdate = models.CharField(max_length=100, default=None)  # 发布时间
    play_volume = models.FloatField()  # 播放量
    barrage = models.CharField(max_length=100, default=None)  # 弹幕数量
    classification = models.CharField(max_length=100, default=None)  # 视频分类
    likes = models.CharField(max_length=100, default=None)  # 点赞数
    coins = models.CharField(max_length=100, default=None)  # 投币数
    collect = models.CharField(max_length=100, default=None)  # 收藏数
    share = models.CharField(max_length=100, default=None)  # 转发数
    url = models.URLField(default='https://www.bilibili.com/')  # 视频地址

    class Meta:
        db_table = 'MUSIC'  # 音乐数据表名

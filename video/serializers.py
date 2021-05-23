from rest_framework.serializers import ModelSerializer
from video.models import MUSIC, DANCE, GAME, KNOWLEDGE, DIGITAL, CAR, LIFE, FOOD, ZOO, ENTERTAINMENT, MOVIES


class MOVIESSerializer(ModelSerializer):
    class Meta:
        model = MOVIES  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class ENTERTAINMENTSerializer(ModelSerializer):
    class Meta:
        model = ENTERTAINMENT  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class ZOOSerializer(ModelSerializer):
    class Meta:
        model = ZOO  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class FOODSerializer(ModelSerializer):
    class Meta:
        model = FOOD  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class LIFESerializer(ModelSerializer):
    class Meta:
        model = LIFE  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class CARSerializer(ModelSerializer):
    class Meta:
        model = CAR  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class DIGITALSerializer(ModelSerializer):
    class Meta:
        model = DIGITAL  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class KNOWLEDGESerializer(ModelSerializer):
    class Meta:
        model = KNOWLEDGE  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class MUSIClSerializer(ModelSerializer):
    class Meta:
        model = MUSIC  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class DANCESerializer(ModelSerializer):
    class Meta:
        model = DANCE  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段


class GAMESerializer(ModelSerializer):
    class Meta:
        model = GAME  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段

from rest_framework.serializers import ModelSerializer
from foreign_currency.models import ForeignCurrency


class ForeignCurrencySerializer(ModelSerializer):
    class Meta:
        model = ForeignCurrency  # 定义序列化器使用哪个模型
        fields = '__all__'  # 要使用该模型中的哪些字段

from house_price import models
from rest_framework.serializers import ModelSerializer


class HousePrice202102Serializer(ModelSerializer):
    class Meta:
        model = models.HousePrice
        fields = '__all__'

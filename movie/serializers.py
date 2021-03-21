from rest_framework.serializers import ModelSerializer
from movie import models


class Movie2011Serializer(ModelSerializer):
    class Meta:
        model = models.Movie2011
        fields = '__all__'

from django.shortcuts import render
from father import view
from house_price.models import HousePrice, HousePrice202104
from house_price.serializers import HousePrice202102Serializer, HousePrice202104Serializer


# Create your views here.
class HousePrice202102ListView(view.ListView):
    def __init__(self, ):
        super().__init__(HousePrice.objects.all(), HousePrice202102Serializer, ['id', 'city'])


class HousePrice202102DetailView(view.DetailView):
    def __init__(self):
        super().__init__(HousePrice.objects.all(), HousePrice202102Serializer)


class HousePrice202104ListView(view.ListView):
    def __init__(self, ):
        super().__init__(HousePrice202104.objects.all(), HousePrice202104Serializer, ['id', 'city'])


class HousePrice202104DetailView(view.DetailView):
    def __init__(self):
        super().__init__(HousePrice202104.objects.all(), HousePrice202104Serializer)

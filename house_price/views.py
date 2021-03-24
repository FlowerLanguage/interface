from django.shortcuts import render
from father import view
from house_price.models import HousePrice
from house_price.serializers import HousePrice202102Serializer


# Create your views here.
class HousePrice202102ListView(view.ListView):
    def __init__(self, ):
        super().__init__(HousePrice.objects.all(), HousePrice202102Serializer, ['id', 'city'])


class HousePrice202102DetailView(view.DetailView):
    def __init__(self):
        super().__init__(HousePrice.objects.all(), HousePrice202102Serializer)

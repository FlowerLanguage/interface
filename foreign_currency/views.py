from django.shortcuts import render
from foreign_currency.serializers import ForeignCurrencySerializer
from foreign_currency.models import ForeignCurrency
from father import view  # 引入自己编写的view父类


# Create your views here.
class ForeignCurrencyListView(view.ListView):
    def __init__(self):
        super().__init__(ForeignCurrency.objects.all(), ForeignCurrencySerializer, ['id', 'symbol'])


class ForeignCurrencyDetailView(view.DetailView):
    def __init__(self):
        super().__init__(ForeignCurrency, ForeignCurrencySerializer)

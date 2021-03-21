from django.shortcuts import render
from lightnovel.models import HotNovel
from lightnovel.serializers import HotNovelSerializer
from father import view  # 引入自己编写的view父类


# Create your views here.
class HotNovelListView(view.ListView):
    def __init__(self):
        super().__init__(HotNovel.objects.all(), HotNovelSerializer, ['id', 'title', 'author'])


class HotNovelDetailView(view.DetailView):
    def __init__(self):
        super().__init__(HotNovel.objects.all(), HotNovelSerializer)

from django.shortcuts import render
from lightnovel.models import HotNovel, UserOperation
from lightnovel.serializers import HotNovelSerializer, UserOperationSerializer
from father import view  # 引入自己编写的view父类


# Create your views here.
class HotNovelListView(view.ListView):
    def __init__(self):
        super().__init__(HotNovel.objects.all(), HotNovelSerializer, ['id', 'title', 'author', 'classification'])


class UserOperationListView(view.ListView):
    def __init__(self):
        super().__init__(UserOperation.objects.all(), UserOperationSerializer, ['id', 'username', 'novel_id'])


class UserOperationDetailView(view.DetailView):
    def __init__(self):
        super().__init__(UserOperation.objects.all(), UserOperationSerializer)


class HotNovelDetailView(view.DetailView):
    def __init__(self):
        super().__init__(HotNovel.objects.all(), HotNovelSerializer)

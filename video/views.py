from django.shortcuts import render
from video.models import MUSIC, DANCE, GAME, KNOWLEDGE, DIGITAL, CAR, LIFE, FOOD, ZOO, ENTERTAINMENT, MOVIES
from video.serializers import MUSIClSerializer, DANCESerializer, GAMESerializer, KNOWLEDGESerializer, DIGITALSerializer, \
    CARSerializer, LIFESerializer, FOODSerializer, ZOOSerializer, ENTERTAINMENTSerializer, MOVIESSerializer
from father import view  # 引入自己编写的view父类


# Create your views here.
class MUSICListView(view.ListView):
    def __init__(self):
        super().__init__(MUSIC.objects.all(), MUSIClSerializer, ['id', 'title', 'author'])


class DANCEListView(view.ListView):
    def __init__(self):
        super().__init__(DANCE.objects.all(), DANCESerializer, ['id', 'title', 'author'])


class GAMEListView(view.ListView):
    def __init__(self):
        super().__init__(GAME.objects.all(), GAMESerializer, ['id', 'title', 'author'])


class KNOWLEDGEListView(view.ListView):
    def __init__(self):
        super().__init__(KNOWLEDGE.objects.all(), KNOWLEDGESerializer, ['id', 'title', 'author'])


class DIGITALListView(view.ListView):
    def __init__(self):
        super().__init__(DIGITAL.objects.all(), DIGITALSerializer, ['id', 'title', 'author'])


class CARListView(view.ListView):
    def __init__(self):
        super().__init__(CAR.objects.all(), CARSerializer, ['id', 'title', 'author'])


class LIFEListView(view.ListView):
    def __init__(self):
        super().__init__(LIFE.objects.all(), LIFESerializer, ['id', 'title', 'author'])


class FOODListView(view.ListView):
    def __init__(self):
        super().__init__(FOOD.objects.all(), FOODSerializer, ['id', 'title', 'author'])


class ZOOListView(view.ListView):
    def __init__(self):
        super().__init__(ZOO.objects.all(), ZOOSerializer, ['id', 'title', 'author'])


class ENTERTAINMENTListView(view.ListView):
    def __init__(self):
        super().__init__(ENTERTAINMENT.objects.all(), ENTERTAINMENTSerializer, ['id', 'title', 'author'])


class MOVIESListView(view.ListView):
    def __init__(self):
        super().__init__(MOVIES.objects.all(), MOVIESSerializer, ['id', 'title', 'author'])

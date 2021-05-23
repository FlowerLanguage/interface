from django.conf.urls import url
from video import views

urlpatterns = [
    url('^MUSIC/$', views.MUSICListView.as_view()),
    url('^DANCE/$', views.DANCEListView.as_view()),
    url('^GAME/$', views.GAMEListView.as_view()),
    url('^KNOWLEDGE/$', views.KNOWLEDGEListView.as_view()),
    url('^DIGITAL/$', views.DIGITALListView.as_view()),
    url('^CAR/$', views.CARListView.as_view()),
    url('^LIFE/$', views.LIFEListView.as_view()),
    url('^FOOD/$', views.FOODListView.as_view()),
    url('^ZOO/$', views.ZOOListView.as_view()),
    url('^ENTERTAINMENT/$', views.ENTERTAINMENTListView.as_view()),
    url('^MOVIES/$', views.MOVIESListView.as_view()),
]

from django.conf.urls import url
from movie import views

patterns = [
    url(r'^movie/2011/$', views.Movie2011ListView.as_view()),
    url(r'^movie/2011/(?P<pk>\d+)/$', views.Movie2011DetailView.as_view()),
]

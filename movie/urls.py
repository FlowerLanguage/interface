from django.conf.urls import url
from movie import views

urlpatterns = [
    url(r'^movie/whole/$', views.MovieWholeListView.as_view()),
    url(r'^movie/whole/(?P<pk>\d+)/$', views.MovieWholeDetailView.as_view()),

    url(r'^movie/2021/$', views.Movie2021ListView.as_view()),
    url(r'^movie/2021/(?P<pk>\d+)/$', views.Movie2021DetailView.as_view()),

    url(r'^movie/2020/$', views.Movie2020ListView.as_view()),
    url(r'^movie/2020/(?P<pk>\d+)/$', views.Movie2020DetailView.as_view()),

    url(r'^movie/2019/$', views.Movie2019ListView.as_view()),
    url(r'^movie/2019/(?P<pk>\d+)/$', views.Movie2019DetailView.as_view()),

    url(r'^movie/2018/$', views.Movie2018ListView.as_view()),
    url(r'^movie/2018/(?P<pk>\d+)/$', views.Movie2018DetailView.as_view()),

    url(r'^movie/2017/$', views.Movie2017ListView.as_view()),
    url(r'^movie/2017/(?P<pk>\d+)/$', views.Movie2017DetailView.as_view()),

    url(r'^movie/2016/$', views.Movie2016ListView.as_view()),
    url(r'^movie/2016/(?P<pk>\d+)/$', views.Movie2016DetailView.as_view()),

    url(r'^movie/2015/$', views.Movie2015ListView.as_view()),
    url(r'^movie/2015/(?P<pk>\d+)/$', views.Movie2015DetailView.as_view()),

    url(r'^movie/2014/$', views.Movie2014ListView.as_view()),
    url(r'^movie/2014/(?P<pk>\d+)/$', views.Movie2014DetailView.as_view()),

    url(r'^movie/2013/$', views.Movie2013ListView.as_view()),
    url(r'^movie/2013/(?P<pk>\d+)/$', views.Movie2013DetailView.as_view()),

    url(r'^movie/2012/$', views.Movie2012ListView.as_view()),
    url(r'^movie/2012/(?P<pk>\d+)/$', views.Movie2012DetailView.as_view()),

    url(r'^movie/2011/$', views.Movie2011ListView.as_view()),
    url(r'^movie/2011/(?P<pk>\d+)/$', views.Movie2011DetailView.as_view()),
]

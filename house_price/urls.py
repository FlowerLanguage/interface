from django.conf.urls import url
from house_price import views

urlpatterns = [
    url(r'^house_price/202102/$', views.HousePrice202102ListView.as_view()),
    url(r'^house_price/202102/(?P<pk>\d+)/$', views.HousePrice202102DetailView.as_view()),
]

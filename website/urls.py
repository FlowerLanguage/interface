from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^blog/$', views.index),
]

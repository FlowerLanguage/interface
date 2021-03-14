from django.conf.urls import url
from foreign_currency import views

urlpatterns = [
    url(r'^foreign_currency/$', views.ForeignCurrencyListView.as_view()),  # 访问主页，展示所有数据
    url(r'^foreign_currency/(?P<pk>\d+)/$', views.ForeignCurrencyDetailView.as_view()),  # 根据输入的id查询，返回一个结果
    url('^(?P<version>[v1|v2]+)/foreign_currency/', views.ForeignCurrencyListView.as_view()),  # 版本路径+想要查询的结果
]

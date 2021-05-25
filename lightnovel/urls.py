from django.conf.urls import url
from lightnovel import views

urlpatterns = [
    url('^hot_novel/$', views.HotNovelListView.as_view()),
    url(r'^hot_novel/(?P<pk>\d+)/$', views.HotNovelDetailView.as_view()),

    url('^operation/$', views.UserOperationListView.as_view()),
    url(r'^operation/(?P<pk>\d+)/$', views.UserOperationDetailView.as_view()),
]

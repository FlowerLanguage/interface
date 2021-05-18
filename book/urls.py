from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^book/$', views.BookListView.as_view()),
    url(r'^book/(?P<pk>\d+)/$', views.BookDetailView.as_view())
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'list$', views.list_files, name='index'),
    url(r'open$', views.open, name='index'),
]

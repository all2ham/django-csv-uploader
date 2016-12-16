from django.conf.urls import url

from . import views


app_name = 'e_up'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
]
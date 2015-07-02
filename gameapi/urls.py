from django.conf.urls import url
from gameapi import views

urlpatterns = [
  url(r'^worlds/$', views.world_list),
  url(r'^worlds/(?P<pk>[0-9]+)/$', views.world_detail),
]

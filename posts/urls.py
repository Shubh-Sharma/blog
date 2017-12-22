from django.conf.urls import include, url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^about/$', about, name="about"),
    url(r'^create/$', post_create, name="add_post"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),
]

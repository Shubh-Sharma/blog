from django.conf.urls import include, url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name="thread"),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name="delete"),
]

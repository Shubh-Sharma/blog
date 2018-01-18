from django.conf.urls import include, url
from django.contrib import admin

from .views import CommentListAPIView, CommentDetailAPIView, CommentCreateAPIView, CommentEditAPIView

urlpatterns = [
    url(r'^create/$', CommentCreateAPIView.as_view(), name="create"),
    url(r'^$', CommentListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="thread"),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name="delete"),
]

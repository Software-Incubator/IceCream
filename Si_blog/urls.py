from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', post_list, name='list'),
    url(r'^create/$',post_create, name='create'),
    url(r'^detail/(?P<id>\d+)/$', post_detail, name='detail'),
    # url(r'^')
]

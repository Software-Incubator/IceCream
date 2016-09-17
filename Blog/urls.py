from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', PostList.as_view(), name='list'),
    url(r'^post_by_tag/(?P<pk>\d+)/$', PostsByTag.as_view(), name='post_by_tag'),
    url(r'^detail/(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    # url(r'^detail/([\d-]+)/$', PostDetail.as_view(), name='detail'),

]

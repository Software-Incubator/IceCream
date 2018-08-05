from .views import IndexView, RegistrationView, BlogView, BlogDetailView, SaveContactView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^savecontact/$', SaveContactView.as_view(), name='save_contact'),
    url(r'^register/$', RegistrationView.as_view(), name='registration'),
    url(r'^blogs/$', BlogView.as_view(), name='blog'),
    url(r'^blogs/(?P<pk>\d+)/detail/$', BlogDetailView.as_view(), name='blog_detail')
]



from .views import IndexView, RegistrationView, BlogView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^register/$', RegistrationView.as_view(), name='registration'),
    url(r'^blogs/$', BlogView.as_view(), name='blog')
]

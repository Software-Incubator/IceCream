from .views import IndexView , Contact_Form, contact_us
from django.conf.urls import url

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^contact_us/$', contact_us, name='contact'),
]
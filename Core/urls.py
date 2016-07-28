from .views import IndexView , Contact_Form
from django.conf.urls import url

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
]
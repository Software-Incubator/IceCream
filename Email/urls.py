from .views import IncomingEmailView
from django.conf.urls import url

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'incoming', csrf_exempt(IncomingEmailView.as_view()), name='incoming_email'),
]

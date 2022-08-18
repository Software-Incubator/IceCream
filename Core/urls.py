from .views import IndexView,  BlogView, BlogDetailView, SaveContactView, FeedbackView, AlumniView, RegistrationView, EmailTemplatesView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^savecontact$', SaveContactView.as_view(), name='save_contact'),
    url(r'^register', RegistrationView.as_view(), name='registration'),
    url(r'^blogs', BlogView.as_view(), name='blog'),
    url(r'^blogs/(?P<pk>\d+)/detail', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^feedback', FeedbackView.as_view(), name='feedback'),
    # url(r'^alumni_registration$', AlumniRegistrationView.as_view(), name='alumni_registration'),
    url(r'^alumni/(?P<batch>[0-9]+)/(?P<slug>[a-zA-Z-]+)/$', AlumniView.as_view(), name='alumni_detail'),
    url(r'^kk/sigret/', EmailTemplatesView.as_view(), name='sigret'),

]

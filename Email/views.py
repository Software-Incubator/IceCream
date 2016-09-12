from django.views.generic import View
from django.http import HttpResponse

class IncomingEmailView(View):
    def post(self, *args, **kwargs):
        print self.request.POST
        return HttpResponse()

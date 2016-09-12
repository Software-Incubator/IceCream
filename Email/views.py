from django.http import HttpResponse
from django.views.generic import FormView

from .forms import EmailForm


class IncomingEmailView(FormView):
    form_class = EmailForm

    def form_valid(self, form):
        form.save()
        return HttpResponse()

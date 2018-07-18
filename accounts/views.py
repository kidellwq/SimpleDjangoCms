from django.shortcuts import render
from django.views.generic import FormView, RedirectView


class RegisterView(FormView):
    template_name = 'account/registration_form.html'

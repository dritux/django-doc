from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def index(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)

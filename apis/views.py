# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

# ----- Main ------------------------------------------------------------------

def index(request):
    return HttpResponse('Hello there, world.')


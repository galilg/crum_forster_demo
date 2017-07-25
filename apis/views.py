# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm
# ----- Main ------------------------------------------------------------------

def index(request):
    return HttpResponse('Hello there, world.')

def nother(request):
    return HttpResponse('You bastards.')


def submit_info(request, info):
    info = info
    return

def yelp_search(request):
    return render(request, 'apis/yelp_search.html', {'form': NameForm})

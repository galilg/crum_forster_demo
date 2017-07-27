# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
# ----- Main ------------------------------------------------------------------

def redirect_root(request):
    return redirect('/apis/')

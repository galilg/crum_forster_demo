# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm

from .api.yelp import test_yelp, Yelp
# ----- Main ------------------------------------------------------------------

def index(request):
    return render(request, 'apis/index.html')
    return HttpResponse('Hello there, world.')

def nother(request):
    return HttpResponse('You bastards.')


def submit_info(request):
    print('This is request: ', dir(request))
    if (request.method == 'POST'):
        print("ITS A POST!!!!")
        input_text = request.POST['your_name']
        address = request.POST['address']
        print(input_text)
        print(address)
    return HttpResponse('submit')

def yelp_search(request):
    #thing = test_yelp.get_test()
    #print(thing)
    return render(request, 'apis/yelp_search.html', {'form': NameForm})

# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm, NumberForm

from .api.yelp import test_yelp, Yelp

from .models import Businesses

import pprint
# ----- Main ------------------------------------------------------------------

def index(request):
    return render(request, 'apis/index.html')
    return HttpResponse('Hello there, world.')

def nother(request):
    return HttpResponse('You bastards.')


def submit_business_name(request):
    if (request.method == 'POST'):
        print("ITS A POST!!!!")
        input_text = request.POST['business_name']
        print("its a business", input_text)
    return HttpResponse('submit')


def submit_phone(request):
    input_text = int(request.POST['phone'])
    print("THis is the phone:", input_text)
    lookup = Yelp.Yelp()
    info = lookup.search_phone(input_text)
    pprint.pprint(info)
    entry = Businesses(name=info['businesses'][0]['name'],
                       street=info['businesses'][0]['location']['address1'],
                       city=info['businesses'][0]['location']['city'],
                       state=info['businesses'][0]['location']['state'],
                       zip_code=info['businesses'][0]['location']['zip_code'])
    entry.save()
    return HttpResponse('submit')


def yelp_search(request):
    #thing = test_yelp.get_test()
    #print(thing)
    return render(request, 'apis/yelp_search.html', {'name_form': NameForm,
                                                     'num_form': NumberForm})

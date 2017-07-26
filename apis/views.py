# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm, NumberForm, LatLongForm

from .api.yelp import test_yelp, Yelp

from .models import Businesses

import pprint
# ----- Main ------------------------------------------------------------------

def index(request):
    return render(request, 'apis/index.html')
    return HttpResponse('Hello there, world.')


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
    business={
    'name':info['businesses'][0]['name'],
    'street':info['businesses'][0]['location']['address1'],
    'city':info['businesses'][0]['location']['city'],
    'state':info['businesses'][0]['location']['state'],
    'zip_code':info['businesses'][0]['location']['zip_code'],
    'phone':info['businesses'][0]['phone'],
    'latitude':info['businesses'][0]['coordinates']['latitude'],
    'longitude':info['businesses'][0]['coordinates']['longitude'],
    'yelp_id':info['businesses'][0]['id'],
    'yelp_rating':info['businesses'][0]['rating'],
    'yelp_price_level':info['businesses'][0]['price'],
    'yelp_no_of_reviews':info['businesses'][0]['review_count']}

    if (len(info['businesses']) > 0):
        #import pdb; pdb.set_trace()
        entry, created = Businesses.objects.update_or_create(
                           yelp_id=info['businesses'][0]['id'],
                           defaults=business,)
        if(created):
            message = "Success, the business has been added to the database."
        else:
            message = "The yelp id already exists in the database. If any data has changed, it's been updated."
    else:
        message = "This number doesn't have any yelp reviews, it was not added."

    return render(request, 'apis/phone_search.html', {'num_form': NumberForm,
                                                      'message': message})
    #return HttpResponse('submit')


def yelp_search(request, search_type):
    #thing = test_yelp.get_test()
    #print(thing)

    if (search_type == '/phone'):
        return render(request, 'apis/phone_search.html', {'num_form': NumberForm})
    elif(search_type == '/lat_long'):
        return render(request, 'apis/lat_long_search.html', {'lat_long_form': LatLongForm})
    elif(search_type == '/location'):
        return render(request, 'apis/location_search.html', {'name_form': NameForm})
    else:
        return render(request, 'apis/yelp_search.html/', {})

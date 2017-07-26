# ----- Imports ---------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm, NumberForm, LatLongForm, AddressForm

from .api.yelp import test_yelp, Yelp
from .api.smarty_streets import SmartyStreets

from .models import Businesses

import pprint
import re
# ----- Main ------------------------------------------------------------------

def index(request):
    return render(request, 'apis/index.html')
    return HttpResponse('Hello there, world.')


def smarty_search(request):
    return render(request, 'apis/smartysearch.html', {'address_form':AddressForm})

def submit_smarty_search(request):
    if (request.method ==  'POST'):
        address = request.POST['street'].strip(' ')
        city = request.POST['city'].strip(' ')
        state = request.POST['state'].strip(' ')
        zip_code = request.POST['zip_code']
        location_smartystreets = {'street':address,
                                   'city':city,
                                   'state':state,
                                   'zipcode':zip_code}

        smarty_streets = SmartyStreets.SmartyStreets()

        info = smarty_streets.check_address(location_smartystreets)

        address_info = {'delivery_line_1': info.delivery_line_1,
                        'primary_number': info.components.primary_number,
                        'street_name': info.components.street_name,
                        'street_suffix':info.components.street_suffix,
                        'city_name':info.components.city_name,
                        'state_abbreviation':info.components.state_abbreviation,
                        'zipcode':info.components.zipcode,
                        'plus4_code':info.components.plus4_code}
        try:
            address_info['street_predirectional'] = info.components.street_predirectional
        except:
            pass
        try:
            address_info['street_postdirectional'] = info.components.street_postdirectional
        except:
            pass

    #else:
    #    address_info = {}
    return render(request, 'apis/smartysearch.html', {'address_form':AddressForm,
                                                      'address_info':address_info})


def submit_business_name(request):
    if (request.method == 'POST'):
        name = request.POST['business_name'].strip(' ')
        address = request.POST['street'].strip(' ')
        city = request.POST['city'].strip(' ')
        state = request.POST['state'].strip(' ')
        zip_code = request.POST['zip_code']
        if (len(state) > 2):
            message = "Please enter standard state abbreviation."
            return render(request, 'apis/location_search.html', {'name_form':NameForm,
                                                                 'message':message})
        location_for_yelp =  city + ', ' + state.upper()
        lookup = Yelp.Yelp()
        info = lookup.search_location(name, location_for_yelp)

        location_smartystreets = {'street':address,
                                      'city':city,
                                      'state':state,
                                      'zipcode':zip_code}

        smarty_streets = SmartyStreets.SmartyStreets()
        smarty_streets_info = smarty_streets.check_address(location_smartystreets)

        ss_street_address = smarty_streets_info.delivery_line_1
        print(ss_street_address)

        if (len(info['businesses']) > 0 and len(info['businesses']) > 2):
            for i in range(0,2):
                yelp_street_address = info['businesses'][i]['location']['address1']
                yelp_location = {'street':yelp_street_address,
                                 'city':city,
                                 'state':state,
                                 'zipcode':zip_code}
                yelp_converted_address = smarty_streets.check_address(yelp_location)
                yelp_street_converted = yelp_converted_address.delivery_line_1
                if(yelp_street_converted == ss_street_address):
                    print('Woohoo we have a match!!')
                    print('Biz id is', info['businesses'][i]['id'])

    return HttpResponse('submit')


def submit_phone(request):
    input_text = request.POST['phone']

    # Remove any non numeric characteres from phone number and
    # strip the leading 1 if it exists.
    input_text = re.sub(r'[^0-9]+', '', input_text).lstrip('1')

    if(len(input_text) < 10 or len(input_text) > 10):
        message = "This doesn't appear to be a valid US number"
        return render(request, 'apis/phone_search.html', {'num_form':NumberForm,
                                                             'message':message})

    input_text = int(input_text)
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
            message = "Success, this business has been added to the database."
            business_name = entry
        else:
            message = "The yelp id already exists in the database. If any data has changed, it's been updated."
            business_name = entry
    else:
        message = "This number doesn't have any yelp reviews, it was not added."

    return render(request, 'apis/phone_search.html', {'num_form': NumberForm,
                                                      'message': message,
                                                      'business_name':business_name})

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

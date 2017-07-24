# ----- Imports ---------------------------------------------------------------

import datetime
import json
import os
import requests
import urllib.parse

# ----- Classes ---------------------------------------------------------------

class Yelp(object):

    '''
    Manages calls the the Yelp API
    '''

    def __init__(self):
        self.__CLIENT_ID = os.environ['YELP_CLIENT_ID']
        self.__CLIENT_SECRET = os.environ['YELP_CLIENT_SECRET']
        self.__ACCESS_TOKEN = None
        self.__load_access_token()
        self.__headers = {'Authorization': 'bearer %s' % self.__ACCESS_TOKEN}
        self.__BASE_URL = 'https://api.yelp.com'

    def __get_new_token(self):
        url = self.__BASE_URL + '/oauth2/token'
        params = {
            'grant_type': 'oauth2',
            'client_id': self.__CLIENT_ID,
            'client_secret': self.__CLIENT_SECRET
        }

        url += '?' + urllib.parse.urlencode(params)
        request = requests.post(url)

        if request.status_code != 200:
            raise RuntimeError(
                'the following request returned a status code of "{}" = "{}"'
                    .format(request.status_code, url))

        content = json.loads(request.content.decode())
        secs_to_expiration = int(content['expires_in'])
        expiration = ( datetime.datetime.now()
                     + datetime.timedelta(seconds = secs_to_expiration) )
        expiration, _, __ = str(expiration).partition('.')
        with open('access_token', 'w') as file:
            file.write(expiration + '\n')
            file.write(content['access_token'])


    def __load_access_token(self):
        try:
            with open('access_token', 'r') as file:
                date = file.readline().rstrip('\n')
                token_expiration = datetime.datetime.strptime(date,
                                                            '%Y-%m-%d %H:%M:%S')
                now  = datetime.datetime.now()
                if (now < token_expiration):
                    self.__ACCESS_TOKEN = file.readline()

                else:
                    self.__get_new_token()
        except:
            self.__get_new_token()


    def __search_businesses(self, name, location=None, lat_long=None):
        url = self.__BASE_URL + '/v3/businesses/search'

        headers = self.__headers #{'Authorization': 'bearer %s' % self.__ACCESS_TOKEN}

        if (location is None):
            params = {
                'term': name,
                'latitude': float(lat_long[0]),
                'longitude': float(lat_long[1]),
                'radius': 5000
            }
        elif(lat_long is None):
            params = {
                'term': name,
                'location': location
            }

        url += '?' + urllib.parse.urlencode(params)
        request = requests.get(url=url, headers=headers)

        #import pdb; pdb.set_trace()
        if request.status_code != 200:
            raise RuntimeError(
                'the following request returned a status code of "{}" = "{}"'
                    .format(request.status_code, url))

        content = json.loads(request.content.decode())
        return content


    def search_location(self, name, location):
        return(self.__search_businesses(name, location))


    def search_lat_long(self, name, lat_long):
        return(self.__search_businesses(name, None, lat_long))


    def search_phone(self, phone):
        url = self.__BASE_URL + '/v3/businesses/search/phone'
        headers = self.__headers
        params = {
            'phone': '+1' + phone
        }
        url += '?' + urllib.parse.urlencode(params)
        request = requests.get(url=url, headers=headers)
        if request.status_code != 200:
            raise RuntimeError(
                'the following request returned a status code of "{}" = "{}"'
                    .format(request.status_code, url))

        content = json.loads(request.content.decode())
        return content


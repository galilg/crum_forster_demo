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


    def __get_new_token(self):
        url = 'https://api.yelp.com/oauth2/token'
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



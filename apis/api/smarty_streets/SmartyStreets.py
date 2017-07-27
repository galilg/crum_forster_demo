# ----- Imports ---------------------------------------------------------------
import os
from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as street_lookup
from smartystreets_python_sdk.us_autocomplete import Lookup as auto_lookup


# ----- Classes ---------------------------------------------------------------

class SmartyStreets(object):
    def __init__(self):
        self.__auth_id = '4f8cb94d-54a4-8bca-509c-3d3ed49c0e8f' #os.environ['SMARTY_AUTH_ID']
        self.__auth_token = 'MV03aBV61mfupgSzc0bq'#os.environ['SMARTY_AUTH_TOKEN']
        self.__credentials = StaticCredentials(self.__auth_id,
                                               self.__auth_token)


    def check_address(self, location):
        client = ClientBuilder(self.__credentials).build_us_street_api_client()
        lookup = street_lookup()
        lookup.street = location['street']
        lookup.city = location['city']
        lookup.state = location['state']
        lookup.zipcode = location['zipcode']

        try:
            client.send_lookup(lookup)
        except exceptions.SmartyExceptions as err:
            print(err)
            return

        result = lookup.result

        if not result:
            return ("No candidates. The address is not valid.")

        candidate = result[0]

        return candidate


    def suggest_address(self, location):
        client = ClientBuilder(self.__credentials).build_us_autocomplete_api_client()
        lookup = auto_lookup(location['address'])
        lookup.add_state_filter(location['state'])
        lookup.max_suggestions = 9

        try:
            suggestions = client.send(lookup)

            return suggestions

        except:
            return("No candidates found.")


# ----- Imports ---------------------------------------------------------------

from .Yelp import Yelp
import pprint

# ----- Main ------------------------------------------------------------------
def get_test(phone):

    yelp = Yelp()

    coord = [40.79654, -74.48156]
    #response = yelp.search_lat_long('Urban Table', coord)
    response = yelp.search_phone(phone)
    return response
    #pprint.pprint(response)

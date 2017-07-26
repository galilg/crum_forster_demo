# ----- Imports ---------------------------------------------------------------

from .Yelp import Yelp
import pprint

# ----- Main ------------------------------------------------------------------
def get_test():

    yelp = Yelp()

    coord = [40.79654, -74.48156]
    #response = yelp.search_lat_long('Urban Table', coord)
    response = yelp.search_phone('2124882626')
    return response
    #pprint.pprint(response)

# ----- Imports ---------------------------------------------------------------

from Yelp import Yelp
import pprint

# ----- Main ------------------------------------------------------------------

yelp = Yelp()

coord = [40.79654, -74.48156]
#response = yelp.search_lat_long('Urban Table', coord)
response = yelp.search_phone('9732675751')
pprint.pprint(response)

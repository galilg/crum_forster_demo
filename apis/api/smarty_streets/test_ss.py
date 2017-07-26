# ----- Imports ---------------------------------------------------------------

from SmartyStreets import SmartyStreets

# ----- Main ------------------------------------------------------------------

ss = SmartyStreets()

location = {'street': '181 W 10 St', 'city':'New York', 'state': 'NY', 'zipcode':'10014'}

responses = ss.check_address(location)

import pprint

pprint.pprint(responses.delivery_line_1)

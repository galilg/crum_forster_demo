# ----- Imports ---------------------------------------------------------------

from SmartyStreets import SmartyStreets

# ----- Main ------------------------------------------------------------------

ss = SmartyStreets()

location = {'address': '181 W 10 St, New York', 'state': 'NY'}
responses = ss.suggest_address(location)

import pprint

for response in responses:
    pprint.pprint(response.text)

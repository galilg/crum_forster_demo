#!/usr/bin/python3

import os

from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_autocomplete import Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_autocomplete_api_client()
    lookup = Lookup("73 Saint Pauls Pl Brooklyn")

    try:
        client.send(lookup)
        print('*** Result with no filter ***')
        print()

    except:
        print("Nothin without filter")

    for suggestion in lookup.result:
        print(suggestion.text)

    lookup.add_state_filter('NY')
    lookup.max_suggestions = 9
    try:

        suggestions = client.send(lookup)  # The client will also return the suggestions directly

        print()
        print('*** Result with some filters ***')

        for suggestion in suggestions:
            print(suggestion.text)
    except:
        print("None found with filter.")

if __name__ == "__main__":
    run()

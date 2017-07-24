import os
from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
    # Uncomment the line above to try it with a proxy instead

    lookup = Lookup()
    lookup.street = "73 St Pauls Place"
    lookup.city = "Brooklyn"
    lookup.state = "NY"
    lookup.zipcode = "11226"

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        print("No candidates. This means the address is not valid.")
        return

    #candidate = result[0]
    for candidate in result:

        print("Address is valid. (There is at least one candidate)\n")
        print("Delivery Line 1:" + candidate.delivery_line_1)
        print("ZIP Code: " + candidate.components.zipcode)
        print("County: " + candidate.metadata.county_name)
        print("Latitude: {}".format(candidate.metadata.latitude))
        print("Longitude: {}".format(candidate.metadata.longitude))

if __name__ == "__main__":
    run()

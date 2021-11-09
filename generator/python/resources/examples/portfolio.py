from __future__ import print_function

import logging
import sys
from pprint import pprint

import criteo_marketing_transition
from criteo_marketing_transition import Configuration

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration(username=sys.argv[1], password=sys.argv[2])

    # Enable/Disable debug httplib and criteo_marketing packages
    # logging.basicConfig(level=logging.DEBUG)
    # configuration.debug = True

    client = criteo_marketing_transition.ApiClient(configuration)

    # Reuse the same client to benefit from the configuration in order to automatically refresh expired token
    advertiser_api = criteo_marketing_transition.AdvertiserApi(client)

    portfolio_response = advertiser_api.api_portfolio_get()
    pprint(portfolio_response)

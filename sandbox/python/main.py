import time
import criteo_api_marketingsolutions_v2022_07
from criteo_api_marketingsolutions_v2022_07.api import advertiser_api
from criteo_api_marketingsolutions_v2022_07.model.get_portfolio_response import GetPortfolioResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_marketingsolutions_v2022_07.Configuration(
    host = "https://api.criteo.com"
)

# Configure OAuth2, two options:
# 1. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
configuration.username = 'YOUR_CLIENT_ID'
configuration.password = 'YOUR_CLIENT_SECRET'

# Set your access token manually, refresh token mechanism IS NOT handled by the client
# configuration.access_token = 'YOUT_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_07.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_portfolio_get()
        pprint(api_response)
    except criteo_api_marketingsolutions_v2022_07.ApiException as e:
        print("Exception when calling AdvertiserApi->api_portfolio_get: %s\n" % e)
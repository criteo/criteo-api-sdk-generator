import time
import criteo_api_marketingsolutions_v2022_07 import ApiClientBuilder
from criteo_api_marketingsolutions_v2022_07.api import advertiser_api
from criteo_api_marketingsolutions_v2022_07.model.get_portfolio_response import GetPortfolioResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.criteo.com
    host = "https://api.criteo.com"

# Configure OAuth2 with client credentials
# refresh token mechanism IS handled for you 💚
clientId = 'YOUR_CLIENT_ID'
clientSecret = 'YOUR_CLIENT_SECRET'

# Enter a context with an instance of the API client
with criteo_api_marketingsolutions_v2022_07.ApiClientBuilder.WithClientCredentials(clientId, clientSecret, host) as api_client:
    # Create an instance of the API class
    api_instance = advertiser_api.AdvertiserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_portfolio_get()
        pprint(api_response)
    except criteo_api_marketingsolutions_v2022_07.ApiException as e:
        print("Exception when calling AdvertiserApi->api_portfolio_get: %s\n" % e)
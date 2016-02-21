from uber_rides.client import UberRidesClient
from uber_rides.auth import AuthorizationCodeGrant


# Uber API Constants
CLIENT_ID = 'HVXgAbDzXyvreW-pctRCHtrvXbYieGD5'
CLIENT_SECRET = '7unYqx257lkRh7Xhbbb-1nlEDTyGKTukEhq_7Cik'
SERVER_TOKEN = 'xPw_C1UY7WlYZKO9B3-Y92hI77sJkHfq3q2pcvq6'
REDIRECT_URI = 'http://localhost:7000/submit'
PERMISSION_SCOPE = 'profile'

'''
# Uber Auth=
auth_flow = AuthorizationCodeGrant(
    CLIENT_ID,
    PERMISSION_SCOPE,
    CLIENT_SECRET,
    REDIRECT_URI)
auth_url = auth_flow.get_authorization_url()

session = auth_flow.get_session()
client = UberRidesClient(session)
credentials = session.oauth2credential
'''


def get_uber_products(start_latitude, start_longitude, redirect_url):
    auth_flow = AuthorizationCodeGrant(
        CLIENT_ID,
        PERMISSION_SCOPE,
        CLIENT_SECRET,
        REDIRECT_URI)
    auth_url = auth_flow.get_authorization_url()

    session = auth_flow.get_session(redirect_url)
    client = UberRidesClient(session)
    credentials = session.oauth2credential

    response = client.get_products(37.77, -122.41)
    products = response.json.get('products')
    print products



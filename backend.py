import requests
from firebase import firebase
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from uber_rides.auth import AuthorizationCodeGrant

#UberAuth
session = Session(server_token=xPw_C1UY7WlYZKO9B3-Y92hI77sJkHfq3q2pcvq6)
#UberUserAuth
auth_flow = AuthorizationCodeGrant(
    YOUR_CLIENT_ID,
    YOUR_PERMISSION_SCOPES,
    YOUR_CLIENT_SECRET,
    YOUR_REDIRECT_URL,
)
auth_url = auth_flow.get_authorization_url()
session = auth_flow.get_session(redirect_url)
client = UberRidesClient(session)
credentials = session.oauth2credential #save credentials in firebase datastore later


#FireBaseAuth
firebase = firebase.FirebaseApplication('https://uberconcierge.firebaseIO.com', None)

#getAvailableProductsFromLocation
def getAvailableProducts():
    client = UberRidesClient(session)
    locationLat = getLocationLat()
    locationLong = getLocationLong()
    response = client.get_products(locationLat, locationLong) #put in lat/long from google maps api on frontend
    products = response.json.get('products')


def getCurrentLocationLat():
    # Returns Lat Long Coordinates
    # From Google Maps API
    latitude = 0
    return latitude

def getCurrentLocationLong():
    longitude = 0;
    return longitude
    
def callUberRide():
    response = client.request_ride(product_id, 37.77, -122.41, 37.79, -122.41)
    ride_details = response.json
    ride_id = ride_details.get('request_id')

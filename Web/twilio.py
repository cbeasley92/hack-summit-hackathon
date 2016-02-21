from twilio.rest import TwilioRestClient
from firebase import firebase

firebase = firebase.FirebaseApplication('https://uberconcierge.firebaseIO.com', None)

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account, token)

def sendMessage():
    message = client.messages.create(to="+12316851234", from_="+15555555555",
                                 body="Hello there!")

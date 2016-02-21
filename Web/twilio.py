from twilio.rest import TwilioRestClient
from firebase import firebase

firebase = firebase.FirebaseApplication('https://uberconcierge.firebaseIO.com', None)

account = "ACe0331ea5a35b43b297aef69a445be390"
token = "bcded206e1255906567f482ad8cf5768"
client = TwilioRestClient(account, token)

def sendMessage():
   message = client.messages.create(to="+12818511567", from_="+17135975622",
                                 body="Hello there!")

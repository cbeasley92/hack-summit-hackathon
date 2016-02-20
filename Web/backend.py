import requests
import os

from firebase import firebase

from flask import Flask, request, json

app = Flask(__name__, static_folder='static', static_url_path='')
app.requests_session = requests.Session()
app.secret_key = os.urandom(24)

# FireBaseAuth
firebase = firebase.FirebaseApplication('https://uberconcierge.firebaseIO.com', None)


@app.route("/coordinates", methods=['POST'])
def post_coordinates():
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    print 'Coordinates: (%s,%s)' % (latitude, longitude)

    return json.dumps({'status': 'OK', 'latitude': latitude, 'longitude': longitude})


@app.route("/coordinates", methods=['GET'])
def get_coordinates():
    latitude = 0
    longitude = 0
    return json.dumps({'status': 'OK', 'latitude': latitude, 'longitude': longitude})


if __name__ == '__main__':
    app.debug = os.environ.get('FLASK_DEBUG', True)
    app.run(port=7000)

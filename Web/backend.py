import requests
import os

from firebase import firebase

from flask import Flask, request, json

import uber_sandbox


# Uber API Constants
CLIENT_ID = 'HVXgAbDzXyvreW-pctRCHtrvXbYieGD5'
CLIENT_SECRET = '7unYqx257lkRh7Xhbbb-1nlEDTyGKTukEhq_7Cik'
SERVER_TOKEN = 'xPw_C1UY7WlYZKO9B3-Y92hI77sJkHfq3q2pcvq6'
REDIRECT_URI = 'http://localhost:7000/submit'
PERMISSION_SCOPE = 'profile'


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


@app.route("/submit", methods=['GET'])
def get_access_code():
    auth_code= request.args.get('code')
    print 'ACCESS_CODE: %s' % auth_code

    redirect_url = '%s?code=%s' % (REDIRECT_URI, auth_code)

    print uber_sandbox.get_uber_products(0, 0, redirect_url)


@app.route("/products", methods=['GET'])
def get_products():
    print uber_sandbox.get_uber_products(0, 0)

if __name__ == '__main__':
    app.debug = os.environ.get('FLASK_DEBUG', True)
    app.run(port=7000)

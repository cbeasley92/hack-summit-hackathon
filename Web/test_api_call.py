import requests

requests.get('http://localhost:7000/')
requests.get('http://localhost:7000/submit')

response = requests.get('http://localhost:7000/price')

print response

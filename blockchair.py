import requests
from requests import get
from pprint import pprint as pp
from matplotlib import pyplot as plt 
from datetime import datetime

BASE_URL = "https://api.blockchair.com/bitcoin/stats"
response = requests.get(BASE_URL)
print(response)
print(response.status_code)
#print(pp(response.json()))









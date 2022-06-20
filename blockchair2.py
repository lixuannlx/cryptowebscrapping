import requests
import json
import pandas as pd 
from urllib.request import urlopen
import pprint as pp
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
#the input dialog
btc_address = simpledialog.askstring(title="Bitcoin Address",
                            prompt="What's your bitcoin transaction address?")

hash_address = simpledialog.askstring(title="Hash Address",
                            prompt="What's your hash addresses?")

def transaction_address_details():
    transaction_address_endpoint = f'https://api.blockchair.com/bitcoin/dashboards/address/{btc_address}?transaction_details=true'
    #https://api.blockchair.com/bitcoin/dashboards/address/bc1q34aq5drpuwy3wgl9lhup9892qp6svr8ldzyy7c?transaction_details=true

    transaction_address_source = requests.get(transaction_address_endpoint)
    transaction_data = transaction_address_source.json()
    pp.pprint(transaction_data)
    #transaction_details = transaction_data['data'][btc_address]['transactions']
    #hashes = json_extract(transaction_details.json(), 'hash')
    #print(hashes)

#data = json.loads(address_source.text)
#txs_hash = data['data'][btc_address]['transactions']

def hash_transaction_details():
    hash_transaction_endpoint = f'https://api.blockchair.com/bitcoin/dashboards/transactions/{hash_address}'
    #https://api.blockchair.com/bitcoin/dashboards/transactions/6531ca04453834d348444cfe8792e5b9d230b9ca8ec71976030ed30d86836cd9

    hash_address_source = requests.get(hash_transaction_endpoint)
    hash = hash_address_source.json()
    pp.pprint(hash)

transaction_address_details()
hash_transaction_details()






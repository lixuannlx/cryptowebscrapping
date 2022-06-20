import requests
import json
import pandas as pd 
from urllib.request import urlopen
import pprint as pp
import tkinter as tk
from tkinter import *

#ROOT = tk.Tk()
#ROOT.withdraw()
#the input dialog
#btc_address = simpledialog.askstring(title="Bitcoin Address",
 #                           prompt="What's your bitcoin transaction address?")

#hash_address = simpledialog.askstring(title="Hash Address",
 #                           prompt="What's your hash addresses?")

def btn_clicked():
    print("Button Clicked")


window = tk.Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    -183.5, -46.5,
    text = "Enter Your Ethereum Wallet Address : ",
    fill = "#000000",
    font = ("Sansation-Bold", int(30.0)))

canvas.create_text(
    35.0, 45.5,
    text = "submit",
    fill = "#ffffff",
    font = ("Sansation-Bold", int(20.0)))

window.resizable(False, False)
window.mainloop()

def transaction_address_details():
    transaction_address_endpoint = f'https://api.blockchair.com/bitcoin/dashboards/address/{btc_address}?transaction_details=true'
    #https://api.blockchair.com/bitcoin/dashboards/address/bc1q34aq5drpuwy3wgl9lhup9892qp6svr8ldzyy7c?transaction_details=true

    transaction_address_source = requests.get(transaction_address_endpoint)
    transaction_data = transaction_address_source.json()
    #pp.pprint(transaction_data)
    hash_details = transaction_data['data'][btc_address]['transactions']
    #hashes = json_extract(transaction_details.json(), 'hash')
    pp.pprint(hash_details)

#data = json.loads(address_source.text)
#txs_hash = data['data'][btc_address]['transactions']

def hash_transaction_details():
    hash_transaction_endpoint = f'https://api.blockchair.com/bitcoin/dashboards/transactions/{hash_address}'
    #https://api.blockchair.com/bitcoin/dashboards/transactions/6531ca04453834d348444cfe8792e5b9d230b9ca8ec71976030ed30d86836cd9

    hash_address_source = requests.get(hash_transaction_endpoint)
    hash = hash_address_source.json()
    pp.pprint(hash)

transaction_address_details()
#hash_transaction_details()






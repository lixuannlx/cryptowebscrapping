from requests import get
from matplotlib import pyplot as plt 
from datetime import datetime

API_KEY = "XDT1SKQW57X4W5A52VAXNGNIFF4W3DQS5A"

'''https://api.etherscan.io/api
   ?module=account
   &action=balancehistory
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &blockno=8000000
   &apikey=YourApiKeyToken'''

BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10**18

def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url


def get_account_balance(address):
    get_balance_url = make_api_url("account", "balance", address, tag="latest", x="2")
    response = get(get_balance_url)
    data = response.json()

    value = int(data["result"])/ ETHER_VALUE
    return value 


'''https://api.etherscan.io/api
   ?module=account
   &action=txlist
   &address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken'''

def get_transaction(address):
    get_transactions_url = make_api_url("account", "txlist", address, startblock=0, endblock=9999999, page=1, offset=10000, sort="asc")
    response = get(get_transactions_url)
    data = response.json()["result"]
    print(get_transactions_url)
    print(data[0])
    
    for tx in data:
        to = tx["to"]
        from_addr = tx["from"]
        value = int(tx["value"]) / ETHER_VALUE
        gas = int(tx["gasUsed"]) * int(tx["gasPrice"]) / ETHER_VALUE
        time = datetime.fromtimestamp(int(tx["timeStamp"]))
        print("To:", to)
        print("From", from_addr)
        print("Value:", value)
        print("Gas Cost:", gas)
        print("Time:", time)


address= "0x73bceb1cd57c711feac4224d062b0f6ff338501e"
get_transaction(address)

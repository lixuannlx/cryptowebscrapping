import requests
import pprint as pp

response = requests.get("https://api.blockchair.com/bitcoin/dashboards/address/bc1q34aq5drpuwy3wgl9lhup9892qp6svr8ldzyy7c?transaction_details=true")
data = response.json()
pp.pprint(data)
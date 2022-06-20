from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd
import pyautogui

import requests
import pprint as pp

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
#the input dialog
USER_INP = simpledialog.askstring(title="Bitcoin Address",
                            prompt="What's your bitcoin transaction address?")

url = "https://blockchair.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get(url)
time.sleep(3)
input_address = driver.find_element(By.XPATH, '//*[@id="searchbar__input"]').send_keys(USER_INP)
pyautogui.press("enter")

#workaround 
bitcoin_transaction = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[3]/div[1]/div/a[1]').click()

click_api = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/section/div[1]/div/h1/div/label[2]/a').click()
transaction_url = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/section/div[1]/div/h1/div/div[2]/div/label/textarea').text

#print(transaction_url)
response = requests.get(transaction_url)
data = response.json()
pp.pprint(data)



#1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa             
#bc1q34aq5drpuwy3wgl9lhup9892qp6svr8ldzyy7c
#blockid   
#Block Hash         
#Date (maybe not needed because time provide date as well)
#time       
#TransactionHash

#Transaction Index
#Gas 
#Gas (ETH)
#Gas Price 
#Gas Price(ETH)
#Error Status 
#Input
#Contract Address
#Gas Used 
#Gas USed (ETH)
#Cummulative Gas USed 
#Cummulative Gas USed (ETH)
#comfirmations 
#method
#from (where?)
#To (where?)
#Value (ETH)
#Txn Fee(ETH)


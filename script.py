import requests
import json
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# filters given by gemini to let me visit the site without saying I m a bot 
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
id_pret = "numField"

# code written by me 

def dis_message(btc_price):
    # REPLACE THIS URL WITH YOUR ACTUAL WEBHOOK LOCALLY
    
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL_HERE"
    
    if btc_price > 75500:
        message = {"content": f"The price is higher than 75500. Current price: {btc_price}"}
        requests.post(webhook_url, json=message)

# This is where the madness begins
def selenium_part():

    driver.get("https://preev.com")
    time.sleep(5)
    
    elementpret = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, id_pret))
    )
    
    pretul_raw = elementpret.get_attribute("value")
    
    pretul = float(pretul_raw)
    
    print(f"Price found: {pretul}")

    dis_message(pretul)

if __name__ == "__main__":
    selenium_part()

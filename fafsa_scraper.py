from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
import vonage

url = 'https://studentaid.gov/h/apply-for-aid/fafsa'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

client = vonage.Client(key=os.environ['NEXMO_API_KEY'], secret=os.environ['NEXMO_API_SECRET'])
sms = vonage.Sms(client)


while True:
 driver.get(url)

 clock = time.time()
 ctime = time.ctime(clock)

 time.sleep(5)

 html = driver.page_source

 soup = BeautifulSoup(html, 'html.parser')

 buttons = soup.find_all('div', {'class': 'fsa-button'})

 if buttons:
     message = "form available"
     sms.send_message({
        'from': 'NUMBER',
        'to': 'NUMBER',
        'text': "FAFSA available!"
     })
 else:
     message = "not available"

 print(message + " - " + ctime)

 time.sleep(15)

driver.quit()

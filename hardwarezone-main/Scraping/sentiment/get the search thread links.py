from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

dir_path = os.path.dirname(os.path.realpath(__file__))
save_thread_path = dir_path + "/" +"sentiment_links.csv"
csvFile = open( save_thread_path, "a", newline='', encoding="utf-8-sig")
csvWriter = csv.writer(csvFile)

# loop through townlist and get threads for each town
townlist = ['ang mo kio', 'bedok', 'bishan', 'bukit batok', 'bukit merah',
       'bukit panjang', 'bukit timah', 'central area', 'choa chu kang',
       'clementi', 'geylang', 'hougang', 'jurong east', 'jurong west',
       'kallang/whampoa', 'marine parade', 'pasir ris', 'punggol',
       'queenstown', 'sembawang', 'sengkang', 'serangoon', 'tampines',
       'toa payoh', 'woodlands', 'yishun']


URL = "https://www.hardwarezone.com.sg/search/forum/"
# custom counter

for town in townlist:
       # append to end of URL
       URLtown = URL + town 
       print(town)
       driver.get(URLtown)
       
       try:
              # skip ad
              time.sleep(2)
              skip = driver.find_element("xpath","//a[contains(@id,'btn_close')]")
              skip.click()
       except:
              pass
       
       count = 0
       for i in range(9):
              
              results = driver.find_elements("xpath","//a[@class='gs-title']")
              
              linklist = []
              for i in results:
                     linklist.append(i.get_attribute("href"))
              linkset = set(linklist)

              for link in linkset:
                     csvWriter.writerow([link,town])
                     
              a = driver.find_elements("xpath","//div[@class='gsc-cursor-page']")

              a[count].click()
              # print(count)
              print("real",a[count].text)
              count += 1
              time.sleep(1)
       
              

              





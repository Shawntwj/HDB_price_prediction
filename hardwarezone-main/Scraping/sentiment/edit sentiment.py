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
new_save_thread_path = dir_path + "/" +"updated_sentiment_link.csv"
csvFile = open( new_save_thread_path, "a", newline='', encoding="utf-8-sig")
csvWriter = csv.writer(csvFile)

dir_path = os.path.dirname(os.path.realpath(__file__))
thread_csv_file = dir_path + "/" + "sentiment_links.csv"
# forumnname threadtitle threadlink town date

with open(thread_csv_file, encoding="utf8") as file_handler:
    for row in csv.reader(file_handler):
        thread_link = row[0]
        thread_link = thread_link.replace('\ufeff',"")
        town_name = row[1]
        
        driver.get(thread_link)
        time.sleep(3)
        
        forum_list = driver.find_elements("xpath","//ul[contains(@class,'p-breadcrumb')]/li")
        forum_name = forum_list[-1].text        
        title_name = driver.find_element("xpath","//h1[contains(@class,'p-title-value')]").text
        date = driver.find_element("xpath", "//time[contains(@class,'u-dt')]").text
        

        print(forum_name)
        print(title_name)
        print(thread_link)
        print(town_name)
        print(date)
        print()
        
        csvWriter.writerow((forum_name,title_name,thread_link,town_name,date))

    
     

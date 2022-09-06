from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import os
import requests
from bs4 import BeautifulSoup

from pprint import pprint


# this file produces thread.csv from links.csv
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

dir_path = os.path.dirname(os.path.realpath(__file__))
link_csv_path = dir_path + "/" + "links.csv"
save_thread_path = dir_path + "/" +"threads.csv"
csvFile = open( save_thread_path, "a", newline='', encoding="utf-8-sig")
csvWriter = csv.writer(csvFile)

# custom check fields to only get threads that have been recently updated or within the month
# datecheck = ["Monday","Tuesday","Wednesday","Thursday","Friday","Yesterday","Sunday","Today","Aug","Saturday"]

count = 0
with open(link_csv_path) as file_handler:
    for row in csv.reader(file_handler):
        forum_link = row[1]
        forum_title = row[0]

        driver.get(forum_link)
        time.sleep(2)   
        max_page = driver.find_element("xpath","//li[@class='pageNav-page ']/a").get_attribute("innerHTML")

        for j in range(int(max_page)):
            if j == 206:
                break
            time.sleep(5)
            results = driver.find_elements("xpath","//div[@class='structItem-title']/a")
            results_date = driver.find_elements("xpath","//time[@class='structItem-latestDate u-dt']")

            if results_date != results:
                minlen = min(len(results_date),len(results))
            else:
                minlen = len(results_date)
                
            for i in range(minlen):
                link = results[i].get_attribute("href")
                thread_title =  results[i].text
                date = results_date[i].text
                csvWriter.writerow((forum_title,thread_title,link,date))
                
                print(link)
                print("here")
                
            try:
                print('\n',count, " threads scraped")
                print("thread page", j+1 ,"done")
                nextbutton = driver.find_element("xpath","//a[@class='pageNav-jump pageNav-jump--next']")
                nextbutton.click()

            except:
                time.sleep(30)
                nextbutton = driver.find_element("xpath","//a[@class='pageNav-jump pageNav-jump--next']")
                nextbutton.click()

                    
        #     print("all thread in page done")
             

        # print("topic ", forum_title, " done")




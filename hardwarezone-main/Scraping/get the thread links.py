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

csvFile = open("threads.csv", "a", newline='', encoding="utf-8")
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
            if j == 2:
                break
            time.sleep(2)
            results = driver.find_elements("xpath","//div[@class='structItem-title']/a")
            results_date = driver.find_elements("xpath","//time[@class='structItem-latestDate u-dt']")
            for i in range(len(results)):
                count += 1
                link = results[i].get_attribute("href")
                thread_title =  results[i].text
                date = results_date[i].text
                print(link)
                print(thread_title)
                print(date)
                csvWriter.writerow((forum_title,thread_title,link,date))

            try:
                print('\n',count, " threads scraped")
                print("thread page", j+1 ,"done")
                nextbutton = driver.find_element("xpath","//a[@class='pageNav-jump pageNav-jump--next']")
                nextbutton.click()

            except:
                time.sleep(30)
                nextbutton = driver.find_element("xpath","//a[@class='pageNav-jump pageNav-jump--next']")
                nextbutton.click()

            print("all thread done")
            # break

        print("topic ", forum_title, " done")




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta

# this produces post.csv
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get(URL)

# max_page = driver.find_elements_by_xpath("//li[@class='pageNav-page ']/a")[-1]
# max_page.click()
# print(max_page)


# doneLinkFile = open("thread p.csv", "w", newline='', encoding="utf-8")
# csvFile = open("posts.csv", "w", newline='', encoding="utf-8")
# ------comment out above line and use the below line if you wish to add on to existing excel file and vice versa----------
csvFile = open("posts.csv", "a", newline='', encoding="utf-8-sig")
doneLinkFile = open("thread done.csv", "a", newline='', encoding="utf-8-sig")

doneLinkcsvWriter = csv.writer(doneLinkFile)
csvWriter = csv.writer(csvFile)

dir_path = os.path.dirname(os.path.realpath(__file__))
thread_csv_file = dir_path + "/" + "sentiment_links.csv"

# datedict = {"Saturday":"21/8/21","Sunday":"22/8/21","Monday":"23/8/21","Tuesday":"17/8/21","Wednesday":"18/8/21","Thursday":"19/8/21","Friday":"20/8/21","Yesterday":"25/8/21","Today":"26/8/21"}

count = 0
split = 0

with open(thread_csv_file, encoding="utf8") as file_handler:

    # loop through the links
    for row in csv.reader(file_handler):

        
        doneLinkcsvWriter.writerow(row)
        
        thread_link = row[2]
        thread_title = row[1]
        topic_name = row[0]
        town_name = row[3]

        print()
        print('topic is now: ', topic_name, " : " , thread_title)
        print("looking at: " , thread_link)

        print(thread_link)
        driver.get(thread_link)
        time.sleep(5)

        # find the number of pages 
        try:
            max_page = driver.find_elements("xpath","//li[@class='pageNav-page ']/a")[-1].get_attribute("innerHTML")
            last_page = driver.find_elements("xpath","//li[@class='pageNav-page ']/a")[-1]
        except:
            max_page = 1
            last_page = ""

        print("this thread has" ,max_page, "pages")

        # go to the last page for recent post
        if last_page:
            last_page.click()

        # loop according to the number of pages in thread
        for i in range(int(max_page)):
            time.sleep(5)
            results = driver.find_elements("xpath","//div[@class='message-inner']")
            # loop according to the number of posts in one page
            for result in results:
                # scrape the information from the post
                try:
                    membername = result.find_element("xpath",".//h4[@class='message-name']").text
                    memberlink = result.find_element("xpath",".//h4[@class='message-name']/a").get_attribute("href")
                    usertitle = result.find_element("xpath",".//h5[@class='userTitle message-userTitle']").text
                    content = result.find_element("xpath",".//div[@class='bbWrapper']").text
                    date = result.find_element("xpath",".//time").text

                    csvWriter.writerow((topic_name, thread_title, thread_link ,membername,memberlink,usertitle,date,content,town_name))

                # skip post if there is missing information Eg deleted content
                except:
                    pass
                
#                 # week control stop scraping the thread and exit thread
#                 if this_week:
#                     pass
#                 else:
#                     break 
            print("thread page", i+1 ,"done")

            try: 
                nextbutton = driver.find_element("xpath","//a[@class='pageNav-jump pageNav-jump--prev']")
                nextbutton.click()
            except:
                print("all of thread done")
                break
            
        count+=1
        print(count, " threads done")
    print("---------------all of topics done---------------")

# csvFile.close()
# driver.close()

# plan is to only extract out the last page of the forums
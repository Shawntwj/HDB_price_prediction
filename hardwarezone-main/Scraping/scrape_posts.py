from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta

# this produces post.csv
URL = "https://forums.hardwarezone.com.sg/threads/qoo10-deals-strictly-no-referral-link-part-7.6132804/"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

doneLinkFile = open("thread p.csv", "w", newline='', encoding="utf-8")
csvFile = open("posts.csv", "w", newline='', encoding="utf-8")
# ------comment out above line and use the below line if you wish to add on to existing excel file and vice versa----------
# csvFile = open("posts.csv", "a", newline='', encoding="utf-8")
# doneLinkFile = open("thread p.csv", "a", newline='', encoding="utf-8")

doneLinkcsvWriter = csv.writer(doneLinkFile)
csvWriter = csv.writer(csvFile)

dir_path = os.path.dirname(os.path.realpath(__file__))
thread_csv_file = dir_path + "/" + "threads.csv"

datedict = {"Monday":"16/8/21","Tuesday":"17/8/21","Wednesday":"11/8/21","Thursday":"12/8/21","Friday":"13/8/21","Yesterday":"17/8/21","Sunday":"15/8/21","Today":"18/8/21"}
count = 0

with open(thread_csv_file, encoding="utf8") as file_handler:
    for row in csv.reader(file_handler):

        doneLinkcsvWriter.writerow(row)
        thread_link = row[2]
        thread_title = row[1]
        topic_name = row[0]

        print()
        print('topic is now: ', topic_name, " : " , thread_title)
        print("looking at: " , thread_link)

        driver.get(thread_link)
        time.sleep(2)

        # scrape one page
        try:
            max_page = driver.find_elements_by_xpath("//li[@class='pageNav-page ']/a")[-1].get_attribute("innerHTML")
        except:
            max_page = 1

        print("this thread has" ,max_page, "pages")
        for i in range(int(max_page)):
            time.sleep(3)
            results = driver.find_elements_by_xpath("//div[@class='message-inner']")
            # print(results[0].get_attribute("innerHTML"))

            # scrape post and post in csv
            for result in results:
                try:
                    membername = result.find_element_by_xpath(".//h4[@class='message-name']").text
                    memberlink = result.find_element_by_xpath(".//h4[@class='message-name']/a").get_attribute("href")
                    usertitle = result.find_element_by_xpath(".//h5[@class='userTitle message-userTitle']").text
                    content = result.find_element_by_xpath(".//div[@class='bbWrapper']").text

                    date = result.find_element_by_xpath(".//time").text

                    # reformat date as it is in a weird string format with words like today tuesday wednesday ect
                    try:
                        date_list = date.split(",")
                        month = date_list[0].split()[0]
                        day= date_list[0].split()[1]
                        year = date_list[1].strip()
                        date_edited = '/'.join((day,month,year))
                        
                    except:
                        try:
                            dayname = date.split()[0]
                            date_edited = datedict[dayname]
                        except:
                            date_edited = datedict["Today"]

                    csvWriter.writerow((topic_name, thread_title, thread_link ,membername,memberlink,usertitle,date_edited,content))
                except:
                    pass
            print("thread page", i+1 ,"done")

            try: 
                nextbutton = driver.find_element_by_xpath("//a[@class='pageNav-jump pageNav-jump--next']")
                nextbutton.click()
            except:
                print("all of thread done")
                break
        
        # manual stop

        # count+=1
        # print(count, " threads done")
        # if count == 4:
        #     break    
    print("---------------all of topics done---------------")

csvFile.close()
driver.close()

# plan is to only extract out the last page of the forums
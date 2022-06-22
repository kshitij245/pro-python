from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrap():
    headers=["name","light_years_from_earth","planet_mass","radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source,"html.parcel")
    for th_tag in soup.find_all("tr",attrs={"class","star"}):
        tr_tagss = th_tag.find_all("li")
        temp_list =[]
        for index,li_tag in enumerate(tr_tagss):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        star_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
   
scrap()

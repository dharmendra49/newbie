# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:41:37 2019

@author: Dharmendra
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
keyWrd=input("Enter the keyword: ")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.itat.gov.in/judicial/casestatus")
keyWord=driver.find_element_by_id("assesse_name")
keyWord.send_keys(keyWrd)
appealType=Select(driver.find_element_by_id("appeal_type"))

appeals=appealType.options
#for appeal in appeals[1:]:
#    print(appeal.text)
appealList=["Income Tax Appeal","Cross Objection","Miscellaneous Application","Wealth Tax Appeal","Stay Application"]

drp=Select(driver.find_element_by_id("bench"))
names= drp.options
state_list=[]
for name in names[1:]:
#    if name.text=="Select":
#        continue
#    else:
        state_list.append(name.text)
#print(state_list)
for state in state_list:
    drp.select_by_visible_text(state)
    time.sleep(1)
    for name in appealList:
        appealType.select_by_visible_text(name)
    #        keyWord=driver.find_element_by_id("assesse_name")
    #        keyWord.clear()
    #        keyWord.send_keys("Tata Capital")
        sbtBtn=driver.find_element_by_xpath('//*[@id="enclosureform"]/table/tbody/tr[2]/td[7]/button')
        sbtBtn.click()
        time.sleep(1)
        appealType=Select(driver.find_element_by_id("appeal_type"))
    drp=Select(driver.find_element_by_id("bench"))    
driver.quit()
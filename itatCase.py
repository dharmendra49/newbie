# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:41:37 2019

@author: Dharmendra
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.itat.gov.in/judicial/casestatus")
time.sleep(5)
drp=Select(driver.find_element_by_id("bench"))
names= drp.options
state_list=[]
for name in names[1:]:
#    if name.text=="Select":
#        continue
#    else:
        state_list.append(name.text)
print(state_list)
        
driver.quit()
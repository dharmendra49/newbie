# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:22:05 2019

@author: Dharmendra
"""

from selenium import webdriver
import time 
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://qacasetrack.cubictree.com/")
time.sleep(5)
login_path="/html/body/div[2]/nav/div/div[2]/ul/li[5]/a"
driver.find_element_by_xpath(login_path).click()
time.sleep(3)
userName=driver.find_element_by_id("UserName")
userName.send_keys("Airtel@cubictree.com")
#time.sleep(3)
userPass=driver.find_element_by_id("Password")
userPass.send_keys('Legal@123')
time.sleep(3)
sumBtn=driver.find_element_by_xpath('//*[@id="example1"]/div/div[2]/form/div[3]/div[1]/input').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/aside[1]/section/ul/li[2]/a').click()
caseNum=driver.find_element_by_id("CaseNumer")
time.sleep(3)
row=len(driver.find_elements_by_xpath('//*[@id="datatable-responsive"]/tbody/tr'))
#print("before: "+str(len(row)))
col=len(driver.find_elements_by_xpath('//*[@id="datatable-responsive"]/tbody/tr[1]/td'))

#caseNum.send_keys("200/2017")
#driver.find_element_by_xpath('//*[@id="Subbut"]').click()
#time.sleep(3)
#print("after: "+str(len(col)))
for r in range(1,row+1):
    for c in range(1,col+1):
        value=driver.find_element_by_xpath('//*[@id="datatable-responsive"]/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(value)
#value=driver.find_element_by_xpath('//*[@id="datatable-responsive"]/tbody/tr[3]/td[5]').text    
#print(value)
driver.quit()

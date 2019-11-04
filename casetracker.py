# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:15:54 2019

@author: Dharmendra
"""

from selenium import webdriver
import time 
driver=webdriver.Chrome()
driver.maximize_window()
def login(UserName):
    driver.get("https://casetrack.cubictree.com/")
    time.sleep(5)
    login_path="/html/body/div[2]/nav/div/div[2]/ul/li[5]/a"
    driver.find_element_by_xpath(login_path).click()
    time.sleep(3)
    userName=driver.find_element_by_id("UserName")
    userName.send_keys(UserName)
    #time.sleep(3)
    userPass=driver.find_element_by_id("Password")
    userPass.send_keys('Legal@123')
    time.sleep(3)
    sumBtn=driver.find_element_by_xpath('//*[@id="example1"]/div/div[2]/form/div[3]/div[1]/input')
    sumBtn.click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside[1]/section/ul/li[2]/a').click()
    time.sleep(3)
def count_word(file_name):
    with open(file_name) as f_obj:
        contents=f_obj.read()
        words=contents.split(",")
#        caseNum=driver.find_element_by_id("CaseNumer") #by case number
        caseNum=driver.find_element_by_id("Title")  #by party name
        for num in words:
            name=num.strip()
            caseNum.send_keys(name)
            driver.find_element_by_xpath('//*[@id="Subbut"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="div-content-list"]/div/div[2]/div/div/div/div/div')
            time.sleep(2)
            row=len(driver.find_elements_by_xpath('//*[@id="datatable-responsive"]/tbody/tr'))
            if row==0:
                print (num)
            caseNum.clear()
    driver.quit()  
login("kvblegal@kvbmail.com")
count_word("karur.txt")    
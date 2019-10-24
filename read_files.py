# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:28:01 2019

@author: Dharmendra
"""
import xlsxwriter 
def write_file(words):
    workbook=xlsxwriter.Workbook('fortune_cnr')
    worksheet=workbook.add_worksheet()  
    row=0
    column=0 
    for word in words:
        worksheet.write(row,column,word)
        row+=1
def read_files(file_name):
    with open(file_name) as file_obj:
        contents=file_obj.read()
        print(contents)
def count_word(file_name):
    with open(file_name) as f_obj:
        contents=f_obj.read()
        words=contents.split(",")
        write_file(words)

#read_files('fort.txt')
count_word('fort.txt')
        
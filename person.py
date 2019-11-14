# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:14:21 2019

@author: Dharmendra
"""

import xlsxwriter 
def count_word(file_name):
    with open(file_name) as f_obj:
        contents=f_obj.read()
        words=contents.split(",")
        List=[]
        for word in words:
            List.append(word)
    return List   
def Diff(li1, li2): 
    row = 0
    column = 0
    new1=list(set(li1) - set(li2))
    for new in new1:
        worksheet.write(row, column, new)
        row+=1
workbook = xlsxwriter.Workbook('newbook1.xlsx') 
worksheet = workbook.add_worksheet()           
newList2=count_word('newCNR.txt')
newList1=count_word('caseT.txt')        
Diff(newList2,newList1)
workbook.close() 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
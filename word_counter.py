# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:00:21 2019

@author: Dharmendra
"""

def count_words(str):
    counts={}
    words=str.split()
    for word in words:
        if word.lower() in counts:
            counts[word]+=1
        else:
            counts[word]=1
    print(counts)       
count_words("the quick brown fox jumps over the lazy dog.")        
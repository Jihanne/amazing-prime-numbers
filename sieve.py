# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:45:53 2018

@author: jihanne
"""
import math

def sieve(n):
    primeList = []
    for i in range(2, n+1):
        primeList.append(i)  
    s = 0 
    j = primeList[s]
    while j <= int((math.sqrt(n))):
        t = 0
        while t <= len(primeList)-1:
            m = primeList[t]
            if m % j == 0 and m is not j:
                primeList.remove(m)
            else:
                t+=1
        s+=1
        j = primeList[s]       
    return primeList 

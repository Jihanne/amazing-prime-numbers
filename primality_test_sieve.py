# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:18:03 2018

@author: jihanne
"""

import math

def prim_sieve(n):
    list = []
    for i in range(2, n+1):
        list.append(i)  
    s = 0 
    j = list[s]
    t = 0
    while j <= int((math.sqrt(n))) and t is not -1:
        if n % j == 0:
            t = -1
        while 0 <= t <= len(list)-1:
            m = list[t]
            if m % j == 0 and m is not j:
                list.remove(m)
            else:
                t+=1
        s+=1
        j = list[s]
    if t is -1:
        return(False)    
    else:
        return(True)

print(prim_sieve(10))
print(prim_sieve(9))
print(prim_sieve(25))
print(prim_sieve(17))
print(prim_sieve(105943)

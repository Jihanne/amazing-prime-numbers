# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:49:37 2018

@author: jihanne
"""
import random

def prim_fermat(n):
    k = 0
    while k <= 2:
        a = random.randint(2, n-2)
        if pow(a, n-1) % n != 1:
            return(False)
            k = 3
        if k is 2 and pow(a, n-1) % n == 1:
            return(True)
        k+=1             
print(prim_fermat(1301081))
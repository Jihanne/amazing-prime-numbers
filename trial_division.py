# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:12:37 2018

@author: jihanne
"""
import math

def prim_trial(n):
    i = 2
    while (i <= math.floor(math.sqrt(n))):
        if (n % i == 0): 
            return False
        i += 1
    return True

print(prim_trial(9))
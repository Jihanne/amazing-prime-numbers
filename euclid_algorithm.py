# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:13:18 2018

@author: jihanne
"""

def gcd(x, y):
    z = x%y
    while z != 0:
        x = y
        y = z
        z = x%y
    return(y)



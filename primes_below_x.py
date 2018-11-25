# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 01:27:23 2018

@author: jihanne
"""
from matplotlib import pyplot as plt

loops = 0
i = 0
primes = []
with open('primes.txt','r') as file:
    for line in file:
        for num in line.split():
           primes.append(num)
           
xlist = []
pi_xlist = []          
for i in range(2, int(primes[len(primes) - 1]) + 2, 1000):
    j = 0
    m = 0
    while j < len(primes) and m is not -1:
        if i <= int(primes[j]):
            m = -1
        else:
            j+=1
    xlist.append(i)
    pi_xlist.append(j)        
    i+=1 
    
plt.title("List of primes below x")
plt.xlabel("x")
plt.ylabel("π(x)")

plt.plot(xlist, pi_xlist)
plt.scatter(xlist, pi_xlist)

plt.show()
    
  

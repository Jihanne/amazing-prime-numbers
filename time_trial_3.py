# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:52:31 2018

@author: jihanne
"""

from sieve import sieve
from trial_division import prim_trial
from primality_test_fermat import prim_fermat
from prettytable import PrettyTable
import time 

primeList = [5, 17, 317, 1733, 46619]
             #104717, 4031399]
             #46891111, 999828727, 9999999929]

s = time.time()
sieveList = sieve(46620) #5 digits
e = time.time()
generate_time = e - s
#sieve is only efficient if you generate the list of primes
#then search it (not recreating the list every time)

sieve_time_list = []
trial_time_list = []
fermat_time_list = []

for i in range (5):
    start1 = time.time()
    if int(primeList[i]) in sieveList:
        m = 1
    else:
        m = 2
    end1 = time.time()
    elapsed1 = end1 - start1  
    sieve_time_list.append(elapsed1)
    
    start2 = time.time()
    prime = prim_trial(int(primeList[i]))
    end2 = time.time()
    elapsed2 = end2 - start2
    trial_time_list.append(elapsed2)
    
    start3 = time.time()
    fermat_prime = prim_fermat(int(primeList[i]))
    end3 = time.time()
    elapsed3 = end3 - start3
    fermat_time_list.append(elapsed3)

myTable = PrettyTable()
myTable.field_names = ['x', 'sieve time', 'trial div time', 'fermat time']

for i in range (5):
    x = primeList[i]
    sieve_time = sieve_time_list[i]
    trial_time = trial_time_list[i]
    fermat_time = fermat_time_list[i]
    myTable.add_row([x, sieve_time , trial_time, fermat_time])
    
print('Sieve generated in ' + str(generate_time) + ' seconds')
print(myTable)

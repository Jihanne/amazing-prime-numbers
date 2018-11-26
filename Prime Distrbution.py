# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:01:25 2018

@author: jihanne
"""
from prettytable import PrettyTable

primes = []
with open('primes.txt','r') as file:
    for line in file:
        for num in line.split():
           primes.append(num)
           
with open('prime_distribution.txt','w+') as file:
    
    #1
    j=0
    for i in range(1000000):
          if int(primes[i]) % 10 == 1:
              j+=1
    file.write(str(j) + ' primes ending with 1\n') 
    
    #3
    j=0
    for i in range(1000000):
          if int(primes[i]) % 10 == 3:
              j+=1
    file.write(str(j) + ' primes ending with 3\n') 
    
    #7
    j=0
    for i in range(1000000):
          if int(primes[i]) % 10 == 7:
              j+=1
    file.write(str(j) + ' primes ending with 7\n') 
    
    #9
    j=0
    for i in range(1000000):
          if int(primes[i]) % 10 == 9:
              j+=1
    file.write(str(j) + ' primes ending with 9\n') 
    file.write('\n')
    
    #1 then 1 -------------------------------------------------------------------
    ends = []
    #1-1, 1-3, 1-7, 1-9, 3-1, 3-3, 3-5, etc
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 1 and int(primes[i+1]) % 10 == 1:
              j+=1
    ends.append(j)
    #1 then 3
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 1 and int(primes[i+1]) % 10 == 3:
              j+=1
    ends.append(j)
    
    #1 then 7
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 1 and int(primes[i+1]) % 10 == 7:
              j+=1
    ends.append(j)
    
    #1 then 9
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 1 and int(primes[i+1]) % 10 == 9:
              j+=1
    ends.append(j)
    
    #3 then 1 ---------------------------------------------------------
    
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 3 and int(primes[i+1]) % 10 == 1:
              j+=1
    ends.append(j)
    #3 then 3
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 3 and int(primes[i+1]) % 10 == 3:
              j+=1
    ends.append(j)
    
    #3 then 7
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 3 and int(primes[i+1]) % 10 == 7:
              j+=1
    ends.append(j)
    
    #3 then 9
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 3 and int(primes[i+1]) % 10 == 9:
              j+=1
    ends.append(j)
    
    #7 then 1 ---------------------------------------------------------
    
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 7 and int(primes[i+1]) % 10 == 1:
              j+=1
    ends.append(j)
    #7 then 3
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 7 and int(primes[i+1]) % 10 == 3:
              j+=1
    ends.append(j)
    
    #7 then 7
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 7 and int(primes[i+1]) % 10 == 7:
              j+=1
    ends.append(j)
    
    #7 then 9
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 7 and int(primes[i+1]) % 10 == 9:
              j+=1
    ends.append(j)
    
    #9 then 1 ---------------------------------------------------------
    
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 9 and int(primes[i+1]) % 10 == 1:
              j+=1
    ends.append(j)
    #9 then 3
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 9 and int(primes[i+1]) % 10 == 3:
              j+=1
    ends.append(j)
    
    #9 then 7
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 9 and int(primes[i+1]) % 10 == 7:
              j+=1
    ends.append(j)
    
    #9 then 9
    j=0
    for i in range(999999):
          if int(primes[i]) % 10 == 9 and int(primes[i+1]) % 10 == 9:
              j+=1
    ends.append(j)
    
    myTable = PrettyTable()
    myTable.field_names = ['prime 1 end', 'prime 2 end', 'no of primes']
    myTable.add_row([1, 1, (ends[0])])
    myTable.add_row([1, 3, (ends[1])])
    myTable.add_row([1, 7, (ends[2])])
    myTable.add_row([1, 9, (ends[3])])
    myTable.add_row([3, 1, (ends[4])])
    myTable.add_row([3, 3, (ends[5])])
    myTable.add_row([3, 7, (ends[6])])
    myTable.add_row([3, 9, (ends[7])])
    myTable.add_row([7, 1, (ends[8])])
    myTable.add_row([7, 3, (ends[9])])
    myTable.add_row([7, 7, (ends[10])])
    myTable.add_row([7, 9, (ends[11])])
    myTable.add_row([9, 1, (ends[12])])
    myTable.add_row([9, 3, (ends[13])])
    myTable.add_row([9, 7, (ends[14])])
    myTable.add_row([9, 9, (ends[15])])
    table_txt = myTable.get_string()
    file.write(table_txt)
    #Twin primes
    j = 0 
    for i in range(999999):
        if int(primes[i+1]) == int(primes[i]) + 2:
            j+=1
    file.write('\nThere are ' + str(j) + ' twin primes.')        
file.close()

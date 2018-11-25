# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:01:25 2018

@author: jihanne
"""
primes = []
with open('primes.txt','r') as file:
    for line in file:
        for num in line.split():
           primes.append(num)

#1
j=0
for i in range(1000000):
      if int(primes[i]) % 10 == 1:
          j+=1
print(str(j) + ' primes ending with 1') 

#3
j=0
for i in range(1000000):
      if int(primes[i]) % 10 == 3:
          j+=1
print(str(j) + ' primes ending with 3') 

#7
j=0
for i in range(1000000):
      if int(primes[i]) % 10 == 7:
          j+=1
print(str(j) + ' primes ending with 7') 

#9
j=0
for i in range(1000000):
      if int(primes[i]) % 10 == 9:
          j+=1
print(str(j) + ' primes ending with 9') 
print()

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

print ('prime 1 end ///', 'prime 2 end ///', 'no of primes')
print('{:0d} {:20d} {:15d}'.format(1, 1, (ends[0])))
print('{:0d} {:20d} {:15d}'.format(1, 3, (ends[1])))
print('{:0d} {:20d} {:15d}'.format(1, 7, (ends[2])))
print('{:0d} {:20d} {:15d}'.format(1, 9, (ends[3])))
print('{:0d} {:20d} {:15d}'.format(3, 1, (ends[4])))
print('{:0d} {:20d} {:15d}'.format(3, 3, (ends[5])))
print('{:0d} {:20d} {:15d}'.format(3, 7, (ends[6])))
print('{:0d} {:20d} {:15d}'.format(3, 9, (ends[7])))
print('{:0d} {:20d} {:15d}'.format(7, 1, (ends[8])))
print('{:0d} {:20d} {:15d}'.format(7, 3, (ends[9])))
print('{:0d} {:20d} {:15d}'.format(7, 7, (ends[10])))
print('{:0d} {:20d} {:15d}'.format(7, 9, (ends[11])))
print('{:0d} {:20d} {:15d}'.format(9, 1, (ends[12])))
print('{:0d} {:20d} {:15d}'.format(9, 3, (ends[13])))
print('{:0d} {:20d} {:15d}'.format(9, 7, (ends[14])))
print('{:0d} {:20d} {:15d}'.format(9, 9, (ends[15])))
print()
#Twin primes
j = 0 
for i in range(999999):
    if int(primes[i+1]) == int(primes[i]) + 2:
        j+=1
print('There are ' + str(j) + ' twin primes.')               

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 01:27:23 2018

@author: jihanne
"""
from matplotlib import pyplot as plt

x_list = []
with open('primes.txt','r') as file:
    for line in file:
        for num in line.split():
           x_list.append(num)
           
pi_xlist = []          
for i in range(0, len(x_list)):
    pi_xlist.append(i)  

fig, ax = plt.subplots( nrows=1, ncols=1 )
ax.plot(x_list, pi_xlist)
ax.set_xlabel('x')
ax.set_ylabel('π(x)')
ax.set_title('List of primes below x')
fig.savefig('pi_x_graph.png')   # save the figure to file
plt.close(fig)    # close the figure        
'''
plt.title("List of primes below x")
plt.xlabel("x")
plt.ylabel("π(x)")

plt.plot(x_list, pi_xlist)
'''
  

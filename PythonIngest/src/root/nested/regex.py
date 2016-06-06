'''
Created on Jun 6, 2016

@author: John
'''
import re
y= list()
nsum=0
hand = open ('regex_sum_257457.txt')

for line in hand:
    stuff = re.findall('[0-9]+', line)
    inp=list(stuff)
    if stuff == []: continue
    for agstuff in stuff:
        nsum = nsum + int(agstuff)
print nsum
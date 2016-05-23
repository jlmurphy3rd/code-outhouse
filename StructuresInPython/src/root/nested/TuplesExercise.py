'''
Created on May 23, 2016

@author: John
'''
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 5 : continue
    if words[0] != "From" : continue 
    when = words[5]
    tics = when.split(":")
    if len(tics) != 3 : continue
    hour = tics[0]
    counts[hour] = counts.get(hour,0) + 1

lst = counts.items()

lst.sort()
for key, val in lst :
    print key, val
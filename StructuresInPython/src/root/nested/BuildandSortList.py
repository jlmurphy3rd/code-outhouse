'''
Created on May 9, 2016

@author: John
'''
fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print'File cannot be opened:',fname
    exit()

lst = list()
for line in fhand:
    word = line.rstrip().split()
    for item in word :
        if item in lst :
            continue
        else :
            lst.append(item)
           
lst.sort()
print lst

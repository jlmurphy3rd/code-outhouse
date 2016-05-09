'''
Created on May 9, 2016

@author: John
'''
fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print 'File cannot be opened', fname
    exit()

count = 0
datalist = list()
for line in fhand:
    if not line.startswith('From:') : continue
    datalist = line.rstrip().split()
    address = datalist[1]
    print address
    count = count + 1
   

print "There were", count, "lines in the file with From as the first word"
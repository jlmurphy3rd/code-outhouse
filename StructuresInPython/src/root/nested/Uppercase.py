'''
Created on May 2, 2016

@author: John
'''
# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print line
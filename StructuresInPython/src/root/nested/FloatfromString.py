'''
Created on May 2, 2016

@author: John
'''
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()
    
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
   
    count = count + 1   
    spind = float(line[20:])
    total += spind
    average = total/count
        
print "Average spam confidence:", average
'''
Created on Apr 23, 2016

@author: John
'''
large = None
small = None

while True:
    Ainput = raw_input("Enter a number: ")
    if Ainput == "done": break
  
    try:
        num = int(Ainput)
    except:
        print "Invalid input"
        continue
        
    if small is None and large is None:
        small = num
        large = num
        
    if num < small:
        small = num
        small = int(small)
                
    if num > large:
        large = num
        large = int(large)
       
# The return sequesnce required "is" in it to be valid. SOB!!!
print "Maximum is", large
print "Minimum is", small
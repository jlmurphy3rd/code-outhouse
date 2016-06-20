'''
Created on Jun 20, 2016

@author: John
'''
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# http://python-data.dr-chuck.net/comments_42.html (sum 2553)
# http://python-data.dr-chuck.net/comments_257462.html (sum #####59)

import urllib
from BeautifulSoup import *
import re

#html = urllib.urlopen('http://python-data.dr-chuck.net/comments_257462.html').read()
url = raw_input("Enter the URL: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')

# open empty list called numbers
numbers = []

for tag in tags:
    # for each line in found file, append only the numbers found  to the list.
    numbers.append(int(tag.string))

# add each integer in the list and print the total.
print sum(numbers)
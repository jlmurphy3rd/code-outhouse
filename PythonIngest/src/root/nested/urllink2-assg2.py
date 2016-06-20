'''
Created on Jun 20, 2016

@author: John
'''
import urllib
from BeautifulSoup import *

#url = raw_input("Enter URL: ")
#count = int(raw_input("Enter count: "))
#position = int(raw_input("Enter position: "))

url = ('http://python-data.dr-chuck.net/known_by_Amelka.html')
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))
names = []

while count > 0:
    print "retrieving: {0}".format(url)
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1

print names[-1]

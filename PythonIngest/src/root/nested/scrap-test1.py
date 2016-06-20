'''
Created on Jun 20, 2016

@author: John
'''
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()   # Read all 
soup = BeautifulSoup(html)
#retrieve a list of the anchor tags
# each tag is like adictionary of HTML attributes

tags = soup('a')     # anchor tags ...just the tags 

for tag in tags:
    print tag.get('href', None)
'''
Created on Jun 27, 2016

@author: John
'''
import urllib2
import xml.etree.ElementTree as ET


def parse_xml(url):
    counts = []
    page = urllib2.urlopen(url)
    tree = ET.parse(page)

    comments = tree.findall('comments/comment')

    for comment in comments:
        counts.append(int(comment.find('count').text))

    return sum(counts)

# Test Data
print parse_xml('http://python-data.dr-chuck.net/comments_42.xml')
# Assignment Data
print parse_xml('http://python-data.dr-chuck.net/comments_257459.xml')

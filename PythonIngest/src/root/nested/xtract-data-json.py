'''
Created on Jul 11, 2016

@author: John
'''
import urllib
import json

place_name = raw_input("Enter a place name: ")
base_url = "http://python-data.dr-chuck.net/geojson?sensor=false&"
address_param = urllib.urlencode({'address': place_name})
target = base_url + address_param

print "Retrieving {0}".format(target)
connection = urllib.urlopen(target)
raw_data = connection.read()
print "Retrieved {0} characters".format(len(raw_data))
parsed_data = json.loads(raw_data)

print "Place id", parsed_data["results"][0]["place_id"]
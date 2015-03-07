#encoding:UTF-8
import urllib, urllib2

url = "http://www.google.com"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()

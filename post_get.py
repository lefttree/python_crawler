import urllib, urllib2


values = {}
values["username"] = ""
values["password"] = ""

data = urllib.urlencode(values)
url = ""

#POST method
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

#GET method
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()




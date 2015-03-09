import urllib2

#URLError
request = urllib2.Request("http://www.wolegequ.com")
try:
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    print e.reason

#HTTPError
#http status
#eg.  200, 404, 403

req = urllib2.Request("http://blog.csdn.net/cqcre")
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    #HTTPError is inherited from URLError
    print e.reason
else:
    print OK



import urllib
import urllib2
import cookielib

filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'stuid':'asdfdsf',
    'pwd': '123123'
    })

loginUrl = 'https://www.ursa.ucla.edu/index.php'
result = opener.open(loginUrl, postdata)

cookie.save(ignore_discard=True,ignore_expires=True)
#some url to check grades, can only see after login
gradeUrl = "safdsaf"

result = opener.open(gradeUrl)
print result.read()

import urllib
import urllib2
import cookielib

filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'uc1e3f003b61290128d4763f80477232e':'',
    'p97e25bce10ebc3b43262330d81f8fc47': ''
    })

headers = {}
user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
#user agent
headers['User-agent'] = user_agent

loginUrl = 'https://auth-asm1.auth.ucla.edu/index.php'
#loginUrl = 'https://auth.ucla.edu/index.php'
request = urllib2.Request(loginUrl, postdata, headers)
result = opener.open(request)
print result.read()

cookie.save(ignore_discard=True,ignore_expires=True)
#some url to check grades, can only see after login
gradeUrl = "https://be.my.ucla.edu/IWE/mygrades.aspx"

result = opener.open(gradeUrl)
print result.read()

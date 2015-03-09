import urllib2
import cookielib
#cookie, some website use to track use identification, track session action...

'''
Opener
before we use urlopen, take url, data, timeout
now we need to create more general opner
'''

'''
Cookielib
'''

#initialize a CookieJar object
cookie = cookielib.CookieJar()
#
handler = urllib2.HTTPCookieProcessor(cookie)
#handler - opener
opener = urllib2.build_opener(handler)
#open method is the same as urlopen, can also use request
url = "http://www.baidu.com"
request = urllib2.Request(url)
response = opener.open(request)
for item in cookie:
    print "Name = " + item.name
    print "Value = " + item.value

# save cookie to file
#FileCookieJar
filename = 'cookie.txt'
cookie_save = cookielib.MozillaCookieJar(filename)
handler_save = urllib2.HTTPCookieProcessor(cookie_save)
opener_save = urllib2.build_opener(handler)
response_save = opener_save.open("http://www.baidu.com")
cookie_save.save(ignore_discard=True, ignore_expires=True)
#ignore_discard: save even cookies set to be discarded. 
#ignore_expires: save even cookies that have expiredThe 
#                file is overwritten if it already exists

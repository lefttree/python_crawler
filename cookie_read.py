import cookielib
import urllib2

def readCookie(file_name, url):
    cookie = cookielib.MozillaCookieJar()
    cookie.load(file_name, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()


if __name__ == "__main__":
    readCookie('cookie.txt', "http://www.baidu.com")

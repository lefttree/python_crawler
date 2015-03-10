import urllib, urllib2
import gzip
import re
import cookielib
import sys


#set header, if not, server may not respond
headers = {}
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
#user agent
headers['User-agent'] = user_agent
#headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' 
#headers['Accept-Encoding'] = 'gzip, deflate, sdch'
#headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'
headers['Connection'] = "keep-alive"
#headers['Host'] = 'www.zhihu.com'
headers['Referer'] = 'http://www.zhihu.com/articles'
#headers['DNT'] = '1'

'''
def get(url, **kwargs):
    if 'data' in kwargs.keys():
        data = kwargs['data']
        if 'timeout' in kwargs.key():
            request = urllib2.Request(url, data, headers, timeout)
        else:
            request = urllib2.Request(url, data, headers)
    else:
        if 'timeout' in kwargs.keys():
            request = urllib2.Request(url, headers, timeout = kwargs['timeout'])
        else:
            request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response
'''

def ungzip(data):
    try:
        print 'ungzip...'
        data = gzip.decompress(data)
        print "ungzip done!"
    except:
        print "no need to ungzip"
    return data

def getXSRF(data):
    #regex to get _xsrf value
    cer = re.compile('name="_xsrf" value="(.*)"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]

def getOpener(head):
    file_name = "cookie.txt"
    cookie = cookielib.MozillaCookieJar(file_name)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener, cookie

if __name__ == "__main__":
    argv = sys.argv[1:]
    url = "http://www.zhihu.com"
    opener, cookie = getOpener(headers)
    try:
        op = opener.open(url)
        cookie.save(ignore_discard=True,ignore_expires=True)
    except urllib2.HTTPError, e:
        print e.code
        print e.reason
    except urllib2.URLError, e:
        print e.reason
    else:
        print "OK"
        
    data = op.read()
    data = ungzip(data)
    print data
    _xsrf = getXSRF(data)
    print _xsrf
    url2 = "http://www.zhihu.com/login"
    id = argv[0]
    password = argv[1]
    print "id is " + id
    print "password is" + password
    postDict = {
            '_xsrf': _xsrf,
            'email': id,
            'password': password,
            'rememberme': 'y'
            }
    postData = urllib.urlencode(postDict)
    data2_op = opener.open(url2, postData)
    data2 = data2_op.read()
    data2 = ungzip(data)
    print "-------------------------------------------------------"
    print "-------------------------------------------------------"
    print "-------------------------------------------------------"
    print "-------------------------------------------------------"
    print data2
    with open("page.html", "w") as file:
        file.write(data2)
    #response = get(url)
    #print response.read()

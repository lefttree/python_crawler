import re
import urllib, urllib2

from collections import deque

queue = deque()
visited = set()

url = "http://news.dbanotes.net"
queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}

    print "got: " + str(cnt) + " getting <--- " + url
    cnt +=1
    request = urllib2.Request(url, timeout = 3)
    #print response.info()['Content-type']
    
    try:
        response = urllib2.urlopen(request)
        if "html" not in response.info()['Content-type']:
            continue
        data = response.read().decode('utf-8')
    except:
        continue

    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print "enque --> " + x

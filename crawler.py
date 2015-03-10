# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

def scrap_page():
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[3])
        if not haveImg:
            print item[0], item[1], item[2], item[4]


page = 1
url = "http://www.qiushibaike.com/hot/page" + str(page)
user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
headers = {'user-agent': user_agent}
try:
    scrap_page()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
    

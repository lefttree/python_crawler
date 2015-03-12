# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

#example url
#http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

class BDTB:

    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "failed to connect to baidu...", e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        #regex to match title tag
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item

if __name__ == "__main__":
    baseURL = "http://tieba.baidu.com/p/3138733512"
    bdtb = BDTB(baseURL, 1)
    page = bdtb.getPage(1)
    title = bdtb.getTitle()
    print title
    num = bdtb.getPageNum()
    print num
    bdtb.getContent(page)

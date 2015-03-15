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
        self.tool = Tool()

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
            print self.tool.replace(item)

class Tool:
    #remove img and 7 consecutive spaces
    removeImg = re.compile('<img.*?>| {7}|')
    #remove a link
    removeLink = re.compile('<a.*?>|</a>')
    #sub tr div p
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #sub td
    replaceTD = re.compile('<td>')
    #sub <p ...> to \n with 2 spaces
    replacePara = re.compile('<p.*?>')
    #sub br with \n
    replaceBR = re.compile('<br><br>|<br>')
    #remove other tags
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeLink, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n  ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()

if __name__ == "__main__":
    baseURL = "http://tieba.baidu.com/p/3138733512"
    bdtb = BDTB(baseURL, 1)
    page = bdtb.getPage(1)
    title = bdtb.getTitle()
    print title
    num = bdtb.getPageNum()
    print num
    bdtb.getContent(page)

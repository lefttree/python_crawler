# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

#example url
#http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

class BDTB:

    def __init__(self, baseUrl, seeLZ, floorTag):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = "baidu forum"
        self.floorTag = floorTag

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

    def getTitle(self, page):
        #regex to match title tag
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode("utf-8"))
        return contents

    def setFileTitle(self, title):
        if title:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeData(self, contents):
        for item in contents:
            if self.floorTag == "1":
                floorLine = "\n" + str(self.floor) + "-----------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if not pageNum:
            print "URL is not valid, please try again"
            return
        try:
            print "This post has " + str(pageNum) + " pages"
            for i in range(1, int(pageNum) + 1):
                print "Writing " + str(i) + " page"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError, e:
            print "IOError " + e.message
        finally:
            print "Task done!"


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
    bdtb = BDTB(baseURL, 1, 1)
    bdtb.start()

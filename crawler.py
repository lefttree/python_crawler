# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
        self.headers = {'user-agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        url = "http://www.qiushibaike.com/hot/page" + str(pageIndex)
        try:
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            html_content = response.read().decode('utf-8')
            return html_content
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getPageItems(self, pageIndex):
        html_content = self.getPage(pageIndex)
        if not html_content:
            print "Failed to load page..."
            return None
        pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, html_content)
        #store stories in every page
        pageStories = []
        for item in items:
            haveImg = re.search("img", item[3])
            if not haveImg:
                #only store stories without img
                #strip() remove whitespace
                pageStories.append([item[0].strip(), item[1].strip(), item[2].strip(), item[4].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            #if num of pages is less than 2, load a new page
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            #wait for enter
            input = raw_input()
            self.loadPage()
            if input == "q":
                self.enable = False
                return 
            print "page %d, publisher: %s, published time: %s \n %s \n like: %s \n" %(page, story[0], story[1], story[2], story[3])

    def start(self):
        print "QSBK Reader"
        print "Enter to read new stories"
        print "Enter 'q' to exit"
        self.enable = True
        self.loadPage()
        curPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                curPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, curPage)

'''
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


try:
    scrap_page()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
'''    
if __name__ == "__main__":
    spider = QSBK()
    spider.start()

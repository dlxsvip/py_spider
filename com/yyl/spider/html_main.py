#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 爬虫总方法
__author__ = 'wb-yyl187231'

from com.yyl.spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        ''' 构造方法 '''
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url):
        count = 1
        # 要爬去的URL添加进URL管理器
        self.urls.add_new_url(root_url)
        # 如果有待爬取的url
        while self.urls.has_new_url():
            try:
                # 取出一个
                new_url = self.urls.get_new_url()
                print '%d : %s' % ( count, new_url)
                # 下载对应的页面
                html_cont = self.downloader.download(new_url)
                # 解析url和数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # URL管理器里添加URLs
                self.urls.add_new_urls(new_urls)
                # 数据收集器
                self.outputer.collect_data(new_data)
                # 爬取1000个URL退出
                if count == 100:
                    break

                count = count + 1
            except Exception, e:
                print('爬取失败')
                print e

        # print self.urls.get_old_urls()
        # 把收集器里的 数据到 HTML
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
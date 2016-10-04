#!/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'wb-yyl187231'

# URL管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self, url):
        ''' 管理器中添加一个URL '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def add_new_urls(self, urls):
        '''管理器中批量添加URL'''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)


    def has_new_url(self):
        '''URL 是否有带爬取的URL'''
        return len(self.new_urls) != 0


    def get_new_url(self):
        '''从管理器中获取一个URL
        pop()从列表中获取并移除
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


    def get_old_urls(self):
        return self.old_urls

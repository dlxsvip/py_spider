#!/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'wb-yyl187231'

import urllib2


# 下载器
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()

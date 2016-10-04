#!/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'wb-yyl187231'

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import re
import urlparse


# 解析器
class HtmlParser(object):
    def __get_new_urls(self, page_url, soup):
        '''爬取URL'''
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            # new_url 按照 page_url格式拼接成全URL
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls


    def __get_new_data(self, page_url, soup):
        ''' 解析数据'''
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # print html_cont
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)

        return new_urls, new_data
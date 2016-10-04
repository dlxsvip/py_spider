#!/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'wb-yyl187231'

# 数据收集器
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        '''收集数据'''
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        '''把数据收集器里的数据写入到HTML'''
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset='utf-8'>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

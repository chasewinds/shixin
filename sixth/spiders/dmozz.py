# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:34:16 2016

@author: Administrator
"""

import scrapy
from sixth.items import DmozItem

#from scrapy.selector import Selector

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://zx.fayi.com.cn"]
    start_urls = [
        "http://zx.fayi.com.cn/debetor?p=1&q=",
        "http://zx.fayi.com.cn/debetor?p=2&q=",
        "http://zx.fayi.com.cn/debetor?p=3&q=",
        "http://zx.fayi.com.cn/debetor?p=4&q=",
        "http://zx.fayi.com.cn/debetor?p=5&q=",
           ]

    def parse(self, response):
        print "parse..."
        print response.body
        # body print successfully
        for herf in response.xpath('/html/body/div/div/div/div'):
            print "first"
            item = DmozItem()
            item['name'] = herf.xpath('div/div/a/text()')
            item['id1'] = herf.xpath('div/div/div/a/text()')
            sel = herf.xpath('div/div/div/a/@href')

        for herf in response.xpath(''):

            item['province'] = herf.xpath('div/div/ul/li/div/table/tbody/tr/td/text()')
            item['eventid'] = herf.xpath('/html/body/div/div/div/div/div/ul/li')
            item['duty'] = herf.xpath('/html/body/div/div/div/div/div/ul/li')
            item['condition'] = herf.xpath('/html/body/div/div/div/div/div/ul/li')
            item['ability'] = herf.xpath('/html/body/div/div/div/ul/li')
            item['time'] = herf.xpath('/html/body/div/div/div/div/div/ul/li')
            print item
                       

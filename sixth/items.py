# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 15:57:33 2016

@author: Administrator
"""

import scrapy

class DmozItem(scrapy.Item):
    name = scrapy.Field()
    id1 = scrapy.Field()
    count = scrapy.Field()
    province = scrapy.Field()
    eventid = scrapy.Field()
    duty = scrapy.Field()
    ability = scrapy.Field()
    time = scrapy.Field()
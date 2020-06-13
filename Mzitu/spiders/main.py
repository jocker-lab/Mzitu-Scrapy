# -*- coding: utf-8 -*-
import scrapy
from fake_useragent import UserAgent
from Mzitu.items import MzituItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    base_url = 'https://www.mzitu.com/'
    userAgent = UserAgent()

    def start_requests(self):
        # 41 - 246
        for page in range(1, 249):
            yield scrapy.Request('{}page/{}'.format(self.base_url, page), headers={'User-Agent': self.userAgent.random}, callback=self.parse_navigation)

    def parse_navigation(self, response):
        names = response.xpath("//img[contains(@class, 'lazy')]/@alt").getall()
        navs = response.xpath("//ul[contains(@id, 'pins')]/li/a/@href").getall()
        for name, nav in zip(names, navs):
            yield scrapy.Request(nav, headers={'User-Agent': self.userAgent.random}, callback=self.parse_girl_max_page, meta={'url': nav})

    def parse_girl_max_page(self, response):
        page_nums = response.xpath("//div[contains(@class, 'pagenavi')]/a/span/text()").getall()

        max_page = max(list(map(int, page_nums[1:-1])))
        url = response.meta['url']
        for i in range(1, max_page):
            yield scrapy.Request('{}/{}'.format(url, i), headers={'User-Agent': self.userAgent.random}, callback=self.parse_pics, meta={'refer': '{}/{}'.format(url, i)})

    def parse_pics(self, response):
        item = MzituItem()
        item['refer'] = response.meta['refer']
        item['url'] = response.xpath("//div[contains(@class, 'main-image')]/p/a/img/@src").get()
        item['name'] = response.xpath("//div[contains(@class, 'main-image')]/p/a/img/@alt").get()
        yield item
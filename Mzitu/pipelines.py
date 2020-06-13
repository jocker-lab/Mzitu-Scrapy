# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import shutil
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from fake_useragent import UserAgent


class ImageDownloadPipeline(ImagesPipeline):

    userAgent = UserAgent()
    img_store = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'], headers={'User-Agent': self.userAgent.random, 'referer': item['refer']})
        return item

    def item_completed(self, results, item, info):

        # 获取抓取成功的图片的基础路径
        base_path = [x['path'] for ok, x in results if ok]
        if not os.path.exists(self.img_store):
            os.makedirs(self.img_store)
        if not os.path.exists(os.path.join(self.img_store, item['name'])):
            os.makedirs(os.path.join(self.img_store, item['name']))
        shutil.move(os.path.join(self.img_store, base_path[0]), os.path.join(self.img_store, item['name'], base_path[0].split('/')[1]))
        return item
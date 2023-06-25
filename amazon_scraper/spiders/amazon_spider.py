import scrapy
import json
import re
from scrapy import cmdline
from urllib.parse import urljoin
from scrapy.crawler import CrawlerProcess
import schedule
import time

class AmazonSpider(scrapy.Spider):
    name = "amazon_spider"

    start_urls = []

    def __init__(self, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.pop('start_urls').split(',')
        print("start urls are ", self.start_urls)

    def start_requests(self):
        print("starting requests ", self.start_urls)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # TODO: Get more data
        # print("response is ", response)
        image_data = json.loads(re.findall(r"colorImages':.*'initial':\s*(\[.+?\])},\n", response.text)[0])
        product_image = image_data[0]['hiRes']
        # variant_data = re.findall(r'dimensionValuesDisplayData"\s*:\s* ({.+?}),\n', response.text)
        feature_bullets = [bullet.strip() for bullet in response.css("#feature-bullets li ::text").getall()]
        price = response.css('.a-price span[aria-hidden="true"] ::text').get("")
        if not price:
            price = response.css('.a-price .a-offscreen ::text').get("")
        yield {
            "name": response.css("#productTitle::text").get("").strip(),
            "price": price,
            "stars": response.css("i[data-hook=average-star-rating] ::text").get("").strip(),
            "rating_count": response.css("div[data-hook=total-review-count] ::text").get("").strip(),
            "feature_bullets": feature_bullets,
            "product_image": product_image,
            # "variant_data": variant_data,
        }

    def crawl(start_urls):
        cmd = "scrapy crawl amazon_spider -a start_urls=" + start_urls
        print(cmd)
        cmdline.execute(cmd.split())
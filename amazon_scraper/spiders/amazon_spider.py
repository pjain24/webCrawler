import scrapy
from ..items import MyItem
import json
import re
from urllib.parse import urljoin

class AmazonSpider(scrapy.Spider):
    name = "amazon_spider"
    start_urls = [
        "https://www.amazon.in/dp/B09P13MTHZ",
        "https://www.amazon.in/dp/B0BS1V2W98"
    ]

    def parse(self, response):
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
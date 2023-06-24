import scrapy
from ..items import MyItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.amazon.in/Tribit-Portable-Multi-Color-Exclusive-Removable/dp/B09P13MTHZ/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=LHfOE&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=M4GRK13A38NWRPR5W350&pd_rd_wg=AkbB5&pd_rd_r=15086303-9efe-49e4-8211-b90c186f976a&pd_rd_i=B09P13MTHZ#customerReviews",
        "https://www.amazon.in/Minimalist-Repairing-Damaged-Complex-Squalane/dp/B0BS1V2W98/ref=pd_vtp_h_pd_vtp_h_sccl_10/262-2562773-2030958?pd_rd_w=Rl4he&content-id=amzn1.sym.ddf0f5ee-c51d-425c-8d75-a37da3720d66&pf_rd_p=ddf0f5ee-c51d-425c-8d75-a37da3720d66&pf_rd_r=JEA4CJ1EQBQHXFGVTVBN&pd_rd_wg=IICnV&pd_rd_r=f03f3c81-8b4a-433a-8ef2-6992f93a86a9&pd_rd_i=B0BS1V2W98&psc=1",
    ]

    def parse(self, response):
        item = MyItem()
        item['title'] = response.css('#productTitle::text').get()
        item['price'] = response.css('#priceblock_ourprice::text').get()
        item['review'] = response.css('.averageStarRatingNumerical a::text').get()
        item['rating'] = response.css('.averageStarRatingNumerical::text').get()
        
        yield item
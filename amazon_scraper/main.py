import streamlit as st
from scrapy.crawler import CrawlerProcess
from spiders.amazon_spider import AmazonSpider
from scrapy import cmdline
import schedule
import time
import os

st.header("Amazon Web Scrapper")

if  __name__ == "__main__":
    start_urls = ["https://www.amazon.in/dp/B09P13MTHZ", "https://www.amazon.in/dp/B0BS1V2W98"]
    os.system('scrapy crawl amazon_spider')
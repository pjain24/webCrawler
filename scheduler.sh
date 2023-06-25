#!/bin/bash
source env/Scripts/activate
cd amazon_scraper
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl amazon_spider
cd ../
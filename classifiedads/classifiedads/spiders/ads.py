import scrapy


class AdsSpider(scrapy.Spider):
    name = "ads"
    allowed_domains = ["classifiedads.com"]
    start_urls = ["https://classifiedads.com"]

    def parse(self, response):
        pass

import scrapy


class AdCategoriesSpider(scrapy.Spider):
    name = "ad_categories"
    allowed_domains = ["classifiedads.com"]
    start_urls = ["https://classifiedads.com"]

    def parse(self, response):
        pass

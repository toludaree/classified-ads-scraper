import scrapy
from itemloaders import ItemLoader
from classifiedads.items import AdCategoriesItem


class AdCategoriesSpider(scrapy.Spider):
    name = "ad_categories"
    allowed_domains = ["classifiedads.com"]
    start_urls = ["https://classifiedads.com"]

    def parse(self, response):
        gallery = response.xpath("//div[contains(@class, 'cat0-')]")
        for category in gallery:
            item = ItemLoader(item=AdCategoriesItem(),
                              response=response, selector=category)

            item.add_xpath("name", "./a/text()")
            item.add_xpath("url", "./a/@href")
            item.add_xpath("subcategories", ".//div[@class='catsublinks']/a/text()")
            item.add_xpath("subcategories", ".//div[@class='catsublinks']/a/@href")

            yield item.load_item()

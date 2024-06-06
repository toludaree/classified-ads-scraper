import scrapy
from itemloaders import ItemLoader
from classifiedads.items import AdCategoriesItem, AdSubCategoriesItem


class AdCategoriesSpider(scrapy.Spider):
    name = "ad_categories"
    allowed_domains = ["classifiedads.com"]
    start_urls = ["https://classifiedads.com"]

    def parse(self, response):
        gallery = response.xpath("//div[contains(@class, 'cat0-')]")
        for category in gallery:
            item = ItemLoader(item=AdCategoriesItem(),
                              response=response, selector=category)

            item.add_xpath("name", "./div/a/text()")
            item.add_xpath("url", "./div/a/@href")
            item.add_value("subcategories", )

            yield item.load_item()
            # item_sub = ItemLoader(item=AdSubCategoriesItem(), response=response, selector=response)

            # item_sub.load_item

    def parse_subcategory(self, response):
        ...

import scrapy
from itemloaders import ItemLoader
from classifiedads.items import AdCategoriesItem


class AdCategoriesSpider(scrapy.Spider):
    name = "ad_categories"
    allowed_domains = ["classifiedads.com"]
    start_urls = ["https://classifiedads.com"]
    
    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)
        settings.set("ITEM_PIPELINES", {}, priority="spider")

    def parse(self, response):
        gallery = response.xpath("//div[contains(@class, 'cat0-')]")
        for category in gallery:
            item = ItemLoader(item=AdCategoriesItem(),
                              response=response, selector=category)

            item.add_xpath("name", "./a/text()")
            item.add_xpath("url", "./a/@href")
            item.add_xpath("subcategories", ".//div[@class='catsublinks']/a")

            yield item.load_item()

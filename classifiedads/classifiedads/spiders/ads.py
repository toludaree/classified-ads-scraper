
from classifiedads.items import ClassifiedadsItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AdsSpider(CrawlSpider):
    name = "ads"
    allowed_domains = ["classifiedads.com"]
    start_urls = ["https://www.classifiedads.com/search.php?keywords=&cid=627&lid=gx2339354&lname=Earth&from=c"]

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths="//div[@class='resultitem']"),
            callback="parse", follow=True
        ),
        Rule(
            LinkExtractor(restrict_xpaths="//a[@class='npage']"),
            callback="parse", follow=True
        ),
    )

    def parse(self, response): 
        item = ItemLoader(item=ClassifiedadsItem(), response=response, selector=response)
        item.add_xpath("title", "//h1[contains(@class, 'itemtitle')]/text()")
        item.add_xpath("city", "//div[span='City:']/span[@class='last']/text()")
        item.add_xpath("phone", "//div[span='Phone:']/span[@class='last']/text()")
        item.add_xpath("zip", "//div[span='Zip:']/span[@class='last']/text()")
        item.add_xpath("description", "//div[@class='description']")   # inner element issue, extracting the html element instead
        item.add_xpath("price", "//div[span='Price:']/span[@class='last']/strong/text()")

        yield item.load_item()

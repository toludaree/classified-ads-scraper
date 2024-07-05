
import json
from classifiedads.items import ClassifiedadsItem
from itemloaders import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AdsSpider(CrawlSpider):
    def __init__(self, *a, **kw):
        super(AdsSpider, self).__init__(*a, **kw)
        self.name = kw.get("name")

        with open("categories.json") as f:   # big vulnerabilty
            categories = json.load(f)
        
        self.cid = categories[self.name]
        self.start_urls = [f"https://www.classifiedads.com/search.php?keywords=&cid={self.cid}&lid=gx2339354&lname=Earth&from=c"]
    
    name = "ads"
    allowed_domains = ["classifiedads.com"]
    # start_urls = ["https://www.classifiedads.com/search.php?keywords=&cid=627&lid=gx2339354&lname=Earth&from=c"]

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
        item.add_xpath("created_date", "//table[@class='listing-properties']//tr[1]/td[2]/text()")
        item.add_xpath("updated_date", "//table[@class='listing-properties']//tr[2]/td[2]/text()")
        item.add_xpath("expires_date", "//table[@class='listing-properties']//tr[3]/td[2]/text()")
        item.add_xpath("views", "//table[@class='listing-properties']//tr[4]/td[2]/text()")
        item.add_xpath("subcategory", "//div[@class='cat1trig']/span[@class='cat1s']/text()")

        yield item.load_item()

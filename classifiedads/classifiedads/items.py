# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from itemloaders.processors import Join, MapCompose
from w3lib.html import replace_tags
from lxml.etree import HTML


def description_in(d):
    return replace_tags(d, "\n")

def clean(d):
    return d[0].strip() \
               .replace("’", "'") \
               .replace("\xa0", " ") \
               .replace("\u200e", "") \
               .replace("  ", " ")

def complete_url(d):
    return "https:" + d

def subcategories_out(d):
    html = HTML(d)
    return {"name": html.xpath("//text()")[0],
            "url":  complete_url(html.xpath("//@href")[0])}


class ClassifiedadsItem(Item):
    title = Field(output_processor=Join())
    city = Field(output_processor=Join())
    phone = Field(output_processor=Join())
    zip = Field(output_processor=clean)   # change to str.strip
    description = Field(input_processor=MapCompose(description_in),
                               output_processor=clean)
    price = Field(output_processor=Join())

class AdCategoriesItem(Item):
    name = Field(input_processor=MapCompose(str.lstrip),
                 output_processor=Join())
    id = Field()
    url = Field(input_processor=MapCompose(complete_url),
                output_processor=Join())
    subcategories = Field(output_processor=MapCompose(subcategories_out))

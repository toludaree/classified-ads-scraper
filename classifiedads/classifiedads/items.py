# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from itemloaders.processors import Join, MapCompose
from w3lib.html import replace_tags


def description_in(d):
    return replace_tags(d, "\n")

def clean(d):
    return d[0].strip() \
               .replace("’", "'") \
               .replace("\xa0", " ") \
               .replace("\u200e", "") \
               .replace("  ", " ")

def url_in(d):
    return "https:" + d


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
    url = Field(input_processor=MapCompose(url_in),
                output_processor=Join())
    subcategories = Field()

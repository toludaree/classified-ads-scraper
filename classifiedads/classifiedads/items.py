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

class ClassifiedadsItem(Item):
    title = Field(output_processor=Join())
    city = Field(output_processor=Join())
    phone = Field(output_processor=Join())
    zip = Field(output_processor=clean)
    description = Field(input_processor=MapCompose(description_in),
                               output_processor=clean)
    price = Field(output_processor=Join())

class AdSubCategoriesItem(Item):
    name = Field()
    id = Field()

class AdCategoriesItem(Item):
    name = Field()
    id = Field()
    subcategories = AdSubCategoriesItem()

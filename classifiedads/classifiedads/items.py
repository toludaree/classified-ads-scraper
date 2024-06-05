# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import replace_tags


def description_in(d):
    return replace_tags(d, "\n")

def clean(d):
    return d[0].strip()

class ClassifiedadsItem(scrapy.Item):
    title = scrapy.Field(output_processor=Join())
    city = scrapy.Field(output_processor=Join())
    phone = scrapy.Field(output_processor=Join())
    zip = scrapy.Field(output_processor=clean)
    description = scrapy.Field(input_processor=MapCompose(description_in),
                               output_processor=clean)
    price = scrapy.Field(output_processor=Join())

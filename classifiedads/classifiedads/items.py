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

def views_in(d):
    return d.split(" ")[0]

def clean(d):
    return d[0].strip() \
               .replace("’", "'") \
               .replace("\xa0", " ") \
               .replace("\u200e", "") \
               .replace("  ", " ")

def complete_url(d):
    return "https:" + d

def get_id_from_url(d):
    options = d.split('?')[1].split('&') # //www.classifiedads.com/search.php?keywords=&cid=470&lid=gx2339354&lname=Earth&from=c
    id = options[1].split('=')[1]
    return id

def subcategories_out(d):
    html = HTML(d)
    name = html.xpath("//text()")[0]
    url = html.xpath("//@href")[0]
    return {"name": name,
            "id": get_id_from_url(url),
            "url":  complete_url(url)}

def id_in(d):
    return d.split()[0].split('-')[1]   # ex: input: "cat0-336 hide", output: "336"


class ClassifiedadsItem(Item):
    title = Field(output_processor=clean)
    city = Field(output_processor=clean)
    phone = Field(output_processor=Join())
    zip = Field(output_processor=clean)   # change to str.strip
    description = Field(input_processor=MapCompose(description_in),
                               output_processor=clean)
    price = Field(output_processor=Join())
    created_date = Field(output_processor=Join())
    updated_date = Field(output_processor=Join())
    expires_date = Field(output_processor=Join())
    views = Field(input_processor=MapCompose(views_in),
                  output_processor=Join())
    subcategory = Field(output_processor=Join())

class AdCategoriesItem(Item):
    name = Field(input_processor=MapCompose(str.lstrip),
                 output_processor=Join())
    id = Field(input_processor=MapCompose(id_in),
               output_processor=Join())
    url = Field(input_processor=MapCompose(complete_url),
                output_processor=Join())
    subcategories = Field(output_processor=MapCompose(subcategories_out))

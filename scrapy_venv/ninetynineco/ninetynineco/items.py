# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose
from w3lib.html import remove_tags

def clean_text(value):
    value = value.replace('\u00b7','-')
    return value

def make_link(value):
    return "https://www.99.co" + value

class ListingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field(input_processor=MapCompose(make_link))
    name = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field(input_processor=MapCompose(clean_text))
    property_type = scrapy.Field()
    lease = scrapy.Field(input_processor=MapCompose(clean_text))
    psf_price = scrapy.Field()
    area = scrapy.Field()
    bedrooms = scrapy.Field(output_processor=TakeFirst())
    bathrooms = scrapy.Field(output_processor=TakeFirst())
    


            # yield {
            #     'link': listing.xpath("./@href").get(),
            #     'name': listing.xpath(".//h3/text()").getall()[0],
            #     'price': listing.xpath(".//h3/text()").getall()[1],
            #     'description': ' '.join(listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[0:2]),
            #     'psf_price': listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[3],
            #     'area': listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[4]
            # }
            # if listing.xpath(".//span[@class='_18I-5']//text()").getall():
            #     yield {
            #         'bedrooms': listing.xpath(".//span[@class='_18I-5']//text()").getall()[0],
            #         'bathrooms': listing.xpath(".//span[@class='_18I-5']//text()").getall()[2]
            #     }
            # else:
            #     yield {
            #         'bedrooms': None,
            #         'bathrooms': None
            #     }


            ## old working code
    # def parse(self, response):
    #     for listing in response.xpath("//a[starts-with(@href,'/singapore/sale/property')]"):
    #         l = ItemLoader(item=ListingItem(), selector=listing)
    #         l.add_xpath('')
    #         yield l.load_item()
    #         yield {
    #             'link': listing.xpath("./@href").get(),
    #             'name': listing.xpath(".//h3/text()").getall()[0],
    #             'price': listing.xpath(".//h3/text()").getall()[1],
    #             'description': ' '.join(listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[0:2]),
    #             'psf_price': listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[3],
    #             'area': listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[4]
    #         }
    #         if listing.xpath(".//span[@class='_18I-5']//text()").getall():
    #             yield {
    #                 'bedrooms': listing.xpath(".//span[@class='_18I-5']//text()").getall()[0],
    #                 'bathrooms': listing.xpath(".//span[@class='_18I-5']//text()").getall()[2]
    #             }
    #         else:
    #             yield {
    #                 'bedrooms': None,
    #                 'bathrooms': None
    #             }
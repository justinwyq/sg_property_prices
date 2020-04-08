import scrapy
from ninetynineco.items import ListingItem
from scrapy.loader import ItemLoader
import re


class NinetyninecoSpider(scrapy.Spider):
    name= 'ninetynineco'


    start_urls = [
        #'https://www.99.co/singapore/sale?page_num=1'
        #'https://www.99.co/singapore/sale/condos-apartments?listing_type=sale&main_category=condo&page_num=1&page_size=35&property_segments=residential&rental_type=unit&sub_categories=condo_apartment&floorarea_min=950&rooms=3%2C4%2C5', #condo and apartment, 3/4/5 room, over 950 sqft
        #'https://www.99.co/singapore/sale/hdb?listing_type=sale&main_category=hdb&page_num=1&page_size=35&sub_categories=hdb_executive', #hdb executive
        #'https://www.99.co/singapore/sale/hdb?listing_type=sale&main_category=hdb&page_num=1&page_size=35&sub_categories=hdb_5r', #hdb 5room
        #'https://www.99.co/singapore/sale/hdb?listing_type=sale&main_category=hdb&page_num=1&page_size=35&sub_categories=hdb_4r', #hdb 4room
        #'https://www.99.co/singapore/sale/houses?listing_type=sale&main_category=landed&page_num=1&page_size=35&property_segments=residential&sub_categories=bungalow%2Cclusterhouse%2Ccorner_terrace%2Cgoodclass_bungalow%2Csemi_detached%2Cterraced_house%2Ctownhouse' #all landed
        'https://www.99.co/singapore/sale/condos-apartments',
        'https://www.99.co/singapore/sale/hdb',
        'https://www.99.co/singapore/sale/executive-condominiums',
        'https://www.99.co/singapore/sale/houses'
    ]



    def parse(self, response):
        for listing in response.xpath("//a[starts-with(@href,'/singapore/sale/property')]"):
            l = ItemLoader(item=ListingItem(), selector=listing)
            raw_listing_link = listing.xpath("./@href").get()
            listing_link = "https://www.99.co" + raw_listing_link[:raw_listing_link.find('?')]
            l.add_value('link',listing_link)
            l.add_xpath('name',"(.//h3/text())[1]")
            l.add_xpath('price',"(.//h3/text())[2]")
            l.add_xpath('address',"(.//p[@class='x0JSc _2eeMf'])[1]/text()")
            l.add_xpath('property_type',"(.//p[@class='x0JSc _2eeMf'])[2]/text()")
            l.add_xpath('lease',"(.//p[@class='x0JSc _2eeMf'])[3]/text()")
            l.add_xpath('psf_price',"(.//p[@class='x0JSc _2eeMf'])[5]/text()")
            l.add_xpath('area',"(.//p[@class='x0JSc _2eeMf'])[6]/text()")
            l.add_xpath('bedrooms',"(.//span[@class='_18I-5'])[1]//text()")
            l.add_xpath('bathrooms',"(.//span[@class='_18I-5'])[2]//text()")
            listing_link = "https://www.99.co" + listing.xpath("./@href").get()
            yield scrapy.Request(listing_link, meta={'listing_item':l.load_item()}, callback=self.parse_listing)
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        
            
    def parse_listing(self, response):
        l = ItemLoader(item=response.meta['listing_item'],selector=response, response=response)#, selector=listing)
        l.add_xpath('description',"//div[@id='description']/pre/text()")
        l.add_xpath('description',"//p[@class='_2sIc2 _29vdm _2rhE-']/text()")
        l.add_xpath('details',"//div[@class='_2Ky0e']//text()")
        l.add_xpath('details',"//div[@class='_3WwZI']//text()")
        l.add_xpath('amenities',"//div[@class='_2M8p3']//text()")
        l.add_xpath('amenities',"//div[@class='_17Tkx']//text()")
        yield l.load_item()
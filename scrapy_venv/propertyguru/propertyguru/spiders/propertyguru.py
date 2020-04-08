import scrapy
from propertyguru.items import ListingItem
from scrapy.loader import ItemLoader
import re







class PropertyGuruSpider(scrapy.Spider):
    name= 'propertyguru'

    #user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    
    download_delay = 2
    start_urls = [
        'https://www.propertyguru.com.sg/property-for-sale'
    ]



    def parse(self, response):

        for listing in response.xpath("//div[starts-with(@class,'listing-card')]"):
            l = ItemLoader(item=ListingItem(), selector=listing)
            listing_link = listing.xpath(".//a[@class='nav-link']/@href").get()

            l.add_value('link',listing_link)
            yield l.load_item()
        #     l.add_value('link',listing_link)
        #     l.add_xpath('name',"(.//h3/text())[1]")
        #     l.add_xpath('price',"(.//h3/text())[2]")
        #     l.add_xpath('address',"(.//p[@class='x0JSc _2eeMf'])[1]/text()")
        #     l.add_xpath('property_type',"(.//p[@class='x0JSc _2eeMf'])[2]/text()")
        #     l.add_xpath('lease',"(.//p[@class='x0JSc _2eeMf'])[3]/text()")
        #     l.add_xpath('psf_price',"(.//p[@class='x0JSc _2eeMf'])[5]/text()")
        #     l.add_xpath('area',"(.//p[@class='x0JSc _2eeMf'])[6]/text()")
        #     l.add_xpath('bedrooms',"(.//span[@class='_18I-5'])[1]//text()")
        #     l.add_xpath('bathrooms',"(.//span[@class='_18I-5'])[2]//text()")
        #     listing_link = "https://www.99.co" + listing.xpath("./@href").get()
        #     yield scrapy.Request(listing_link, meta={'listing_item':l.load_item()}, callback=self.parse_listing)
        next_page = response.xpath("//li[@class='pagination-next']/a/@href").get()
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
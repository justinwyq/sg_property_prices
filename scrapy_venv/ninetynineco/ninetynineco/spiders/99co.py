import scrapy
from ninetynineco.items import ListingItem
from scrapy.loader import ItemLoader

class NinetyninecoSpider(scrapy.Spider):
    name= 'ninetynineco'

    start_urls = [
        'https://www.99.co/singapore/sale?page_num=1'
    ]

    def parse(self, response):
        for listing in response.xpath("//a[starts-with(@href,'/singapore/sale/property')]"):
            l = ItemLoader(item=ListingItem(), selector=listing)
            l.add_xpath('link',"./@href")
            l.add_xpath('name',"(.//h3/text())[1]")
            l.add_xpath('price',"(.//h3/text())[2]")
            l.add_xpath('address',"(.//p[@class='x0JSc _2eeMf'])[1]/text()")
            l.add_xpath('property_type',"(.//p[@class='x0JSc _2eeMf'])[2]/text()")
            l.add_xpath('lease',"(.//p[@class='x0JSc _2eeMf'])[3]/text()")
            l.add_xpath('psf_price',"(.//p[@class='x0JSc _2eeMf'])[5]/text()")
            l.add_xpath('area',"(.//p[@class='x0JSc _2eeMf'])[6]/text()")
            l.add_xpath('bedrooms',"(.//span[@class='_18I-5'])[1]//text()")
            l.add_xpath('bathrooms',"(.//span[@class='_18I-5'])[2]//text()")
            yield l.load_item()

            
    def parse_listing(self, response):
        for listing in response.xpath("//a[starts-with(@href,'/singapore/sale/property')]"):
            l = ItemLoader(item=ListingItem(), selector=listing)
            l.add_xpath('')
            yield l.load_item()
            yield {
                'link': listing.xpath("./@href").get(),
                'name': listing.xpath(".//h3/text()").getall()[0],
                'price': listing.xpath(".//h3/text()").getall()[1],
                'description': ' '.join(listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[0:2]),
                'psf_price': listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[3],
                'area': listing.xpath(".//p[@class='x0JSc _2eeMf']/text()").getall()[4]
            }
            if listing.xpath(".//span[@class='_18I-5']//text()").getall():
                yield {
                    'bedrooms': listing.xpath(".//span[@class='_18I-5']//text()").getall()[0],
                    'bathrooms': listing.xpath(".//span[@class='_18I-5']//text()").getall()[2]
                }
            else:
                yield {
                    'bedrooms': None,
                    'bathrooms': None
                }
            


### example

# def parse(self, response):
#     tables = response.xpath('//table[./tr/td[contains(text(), "members")]]')
#     for table in tables:
#         for href in table.css('tr td a::attr(href)'):
#             yield Request(href, callback=self.parse_member_profile)

# def parse_member_profile(self, response):
#     ...




# https://www.99.co/singapore/sale?listing_type=sale&main_category=hdb&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num=1&page_size=35&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&show_cluster_preview=true&show_future_mrts=true&sub_categories=hdb_4r&zoom=11 #4 room hdb, 93 pages
# https://www.99.co/singapore/sale?listing_type=sale&main_category=hdb&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num=1&page_size=35&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&show_cluster_preview=true&show_future_mrts=true&sub_categories=hdb_5r&zoom=11 #5 room hdb , 69 pages
# https://www.99.co/singapore/sale?listing_type=sale&main_category=hdb&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num=1&page_size=35&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&show_cluster_preview=true&show_future_mrts=true&sub_categories=hdb_executive&zoom=11 #executive hdb, 27 pages

# https://www.99.co/singapore/sale?floorarea_min=1000&listing_type=sale&main_category=condo&map_bounds=1.100319%2C103.535461%2C1.529134%2C104.15871&page_num=1&page_size=35&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&rooms=3%2C4%2C5&show_cluster_preview=false&show_future_mrts=true&sort_field=recency&sort_order=desc&sub_categories=condo_apartment%2Cexecutive_condo%2Cgeneric_condo&zoom=12 # 3, 4, 5 BR Condos, 228 pages

# https://www.99.co/singapore/sale?floorarea_min=1000&listing_type=sale&main_category=landed&map_bounds=1.100319%2C103.535461%2C1.529134%2C104.15871&page_num=1&page_size=35&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&radius_max=1000&rental_type=unit&rooms=3%2C4%2C5&show_cluster_preview=false&show_future_mrts=true&sort_field=recency&sort_order=desc&sub_categories=bungalow%2Cclusterhouse%2Ccorner_terrace%2Cgoodclass_bungalow%2Csemi_detached%2Cterraced_house%2Ctownhouse&zoom=12 # landed excluding "land only", shophouse, conservation house, 201 pages

# XPATH for each listing cards
# //a[starts-with(@href,'/singapore/sale/property')]



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
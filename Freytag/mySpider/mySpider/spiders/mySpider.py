import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        'https://frey-tag.at/kalender?page=1&wo=Wien&was=PARTY'
    ]

    # Custom settings for the spider
    custom_settings = {
        'FEEDS': {
            'dataClean.json': {
                'format': 'json',
                'overwrite': True,  # If the file already exists, it will overwrite it
                'indent': 4,  # Better readable
            },
        },
    }

    def parse(self, response):
        # Extraction basics from the website
        alldata = response.xpath("//body//text()").getall()


        # Creating structure information and add into the JSON file
        yield {
            'data' : alldata
        }
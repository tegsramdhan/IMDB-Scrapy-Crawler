from calendar import c
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider( CrawlSpider ):
    name = "IMDBCrawler"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/boxoffice"]
    
    rules = (
        Rule(LinkExtractor(allow="/title/"), callback= "parse_item" ),
    )

    def parse_item( self, response ):
        yield {
            "Title" : response.css('h1[data-testid="hero-title-block__title"]::text').get(),
            "Year" : response.css('a[class = "ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 iOtMms"]::text').get(),
            "Rating" : response.css('span[class = "sc-7ab21ed2-1 eUYAaq"]::text').get()
        }



    
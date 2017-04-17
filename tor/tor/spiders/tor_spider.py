from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tor.items import SiteItem


class TorSpider(CrawlSpider):
    name = 'tor'
    rules = (
        Rule(
            # Regex for .onion domains
            LinkExtractor(allow_domains=('https?:\/\/[^\/]*\.onion\/')),
            callback='parse_website'
        ),
    )

    def parse_website(self, response):
        print response
        title = response.selector.xpath('/html/head/title/text()').extract()
        item = SiteItem()
        item['url'] = str(response.url)
        item['title'] = title
        yield item

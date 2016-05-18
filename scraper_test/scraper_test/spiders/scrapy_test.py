from scrapy.spiders import Spider
import scrapy
class SpiderTest(Spider):
    name = 'demo'
    allowed_domains = ["fiercepharma.com"]
    start_urls = ["http://www.fiercepharma.com/animal-health"]
    
    def parse(self, res): 
        xpsel = scrapy.Selector(res)
        titles = xpsel.xpath('//div[@class="list-group contextual-region js-view-dom-id-0d75b2dead8b863bf74d25ba5b21b786ecae07cce7180cec80e3debc7d88855b"]')
        for ttl in titles:
            title = ttl.xpath('//h2[@class="field-content__list-title"]/text()')
            link = ttl.xpath("a/@href")
            print titles, title, link

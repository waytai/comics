from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Count Your Sheep'
    language = 'en'
    url = 'http://www.countyoursheep.com/'
    start_date = '2003-06-11'
    rights = 'Adrian "Adis" Ramos'

class Crawler(CrawlerBase):
    history_capable_date = '2003-06-11'
    schedule = 'Mo,Tu,We,Th,Fr'

    def crawl(self, pub_date):
        page_url = 'http://www.countyoursheep.com/d/%s.html' % (
            pub_date.strftime('%Y%m%d'),)
        page = self.parse_page(page_url)
        url = page.src('img[src^="http://www.countyoursheep.com/comics/"]')
        return CrawlerResult(url)

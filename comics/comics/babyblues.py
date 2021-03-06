from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.core.comic_data import ComicDataBase


class ComicData(ComicDataBase):
    name = 'Baby Blues'
    language = 'en'
    url = 'http://www.arcamax.com/babyblues'
    start_date = '1990-01-01'
    rights = 'Rick Kirkman and Jerry Scott'


class Crawler(CrawlerBase):
    history_capable_days = 0
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = 'US/Eastern'

    def crawl(self, pub_date):
        page = self.parse_page('http://www.arcamax.com/babyblues')
        url = page.src('img[alt^="Baby Blues Cartoon"]')
        return CrawlerImage(url)

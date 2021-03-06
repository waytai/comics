from comics.aggregator.crawler import CrawlerBase
from comics.core.comic_data import ComicDataBase


class ComicData(ComicDataBase):
    name = 'Hipster Hitler'
    language = 'en'
    url = 'http://www.hipsterhitler.com/'
    start_date = '2010-08-01'
    end_date = '2013-01-15'
    active = False
    rights = 'JC & APK'


class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        pass  # Comic no longer published

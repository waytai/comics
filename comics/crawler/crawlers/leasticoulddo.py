from comics.crawler.crawlers import BaseComicCrawler
from comics.crawler.meta import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = 'Least I Could Do'
    language = 'en'
    url = 'http://www.leasticoulddo.com/'
    start_date = '2003-02-10'
    history_capable_date = '2003-02-10'
    schedule = 'Mo,Tu,We,Th,Fr,Sa'
    time_zone = -5
    rights = 'Ryan Sohmer & Lar deSouza'

class ComicCrawler(BaseComicCrawler):
    def _get_url(self):
        self.url = 'http://archive.leasticoulddo.com/strips/%(date)s.gif' % {
            'date': self.pub_date.strftime('%Y%m%d'),
        }

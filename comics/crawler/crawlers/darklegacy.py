from comics.crawler.crawlers import BaseComicCrawler

class ComicCrawler(BaseComicCrawler):
    def _get_url(self):
        self.feed_url = 'http://www.darklegacycomics.com/feed.xml'
        self.parse_feed()

        for entry in self.feed['entries']:
            pub_date = self.string_to_date(entry['summary'], 'Updated %m/%d/%y')
            if pub_date == self.pub_date:
                self.title = entry['title']
                self.url = entry['link'].replace('.html', '.jpg')
                return
import urllib.request
from html.parser import HTMLParser


class PageNavigator(HTMLParser):
    def __init__(self, link):
        super(PageNavigator, self).__init__()
        try:
            page = urllib.request.urlopen('http://mg.wikipedia.org' + link)
        except Exception:
            return
        data = page.read().decode('utf-8')
        self.feed(data)
from PageNavigator import PageNavigator
from ArticleParser import ArticleParser
from Answer import Answer


class CatParser(PageNavigator):
    def __init__(self, link):
        self.depth = None
        super(CatParser, self).__init__(link)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs and attrs['id'] == 'mw-pages':
            self.depth = 0
        if self.depth is not None:
            self.depth += 1
            if tag == 'a' and (attrs['title'], attrs['href'] not in Answer.result):
                ArticleParser(attrs['title'], attrs['href'])

    def handle_endtag(self, tag):
        if self.depth is not None:
            self.depth -= 1
            if self.depth == 0:
                self.depth = None
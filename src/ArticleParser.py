from PageNavigator import PageNavigator
from Answer import Answer


class ArticleParser(PageNavigator):
    def __init__(self, name, link):
        self.depth = None
        self.article = (name, link)
        Answer.result[self.article] = 0
        super(ArticleParser, self).__init__(link)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs and attrs['id'] == 'catlinks':
            self.depth = 0
        if self.depth is not None:
            self.depth += 1
            if tag == 'a' and attrs['title'] != 'Manokana:Sokajy':
                Answer.result[self.article] += 1

    def handle_endtag(self, tag):
        if self.depth is not None:
            self.depth -= 1
            if self.depth == 0:
                self.depth = None
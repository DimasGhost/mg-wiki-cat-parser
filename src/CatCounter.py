from PageNavigator import PageNavigator


class CatCounter(PageNavigator):
    categories = []

    def __init__(self, link):
        self.next = None
        super(CatCounter, self).__init__(link)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'class' in attrs and attrs['class'] == 'mw-nextlink':
            self.next = attrs['href']
        if 'title' in attrs and attrs['title'][:7] == 'Sokajy:':
            CatCounter.categories.append(attrs['href'])
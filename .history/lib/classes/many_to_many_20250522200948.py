# many_to_many.py

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        return self._articles.copy()

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, article):
        self._articles.append(article)

    def topic_areas(self):
        return list(set(mag.category for mag in self.magazines()))

    def add_article_to_magazine(self, magazine, title):
        return Article(self, magazine, title)


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles.copy()

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = title
        self.author = author  # uses property setter
        self.magazine = magazine
        Article.all.append(self)
        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title  # immutable

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value

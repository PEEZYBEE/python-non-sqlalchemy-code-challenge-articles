class Article:
    def __init__(self, author, magazine, title):
        # Validate title length 5-50 (optional but suggested)
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine

        # Add this article to author and magazine article lists
        author.articles.append(self)
        magazine.articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("can't set attribute")

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("can't set attribute")

    def add_article(self, magazine, title):
        # Create Article with this author, given magazine and title
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return unique list of magazine categories for all articles by this author
        categories = {article.magazine.category for article in self.articles}
        return list(categories)

    def magazines(self):
        # Return unique list of magazines author has written for
        mags = {article.magazine for article in self.articles}
        return list(mags)

class Magazine:
    def __init__(self, name, category):
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be 2 to 16 characters")
        if len(category) == 0:
            raise ValueError("Category must be non-empty string")

        self.name = name
        self.category = category
        self.articles = []

    def article_titles(self):
        titles = [article.title for article in self.articles]
        return titles if titles else None

    def contributing_authors(self):
        # Authors with more than 2 articles in this magazine
        author_article_count = {}
        for article in self.articles:
            author = article.author
            author_article_count[author] = author_article_count.get(author, 0) + 1

        contributing = [author for author, count in author_article_count.items() if count > 2]
        return contributing if contributing else None

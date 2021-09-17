from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, ARRAY
from sqlalchemy.orm import declarative_base, relationship

from publisher import Publisher

Base = declarative_base()
table_prefix = 'articles_'

class Article(Base):
    __tablename__ = table_prefix + 'article'
    id = Column('id', Integer, primary_key=True)
    url = Column('url', String)
    title = Column('title', String)
    description = Column('description', String)
    authors = Column('authors', ARRAY(String))
    image = Column('image', String)
    publisher = Column('publisher', Integer, ForeignKey(Publisher.id))
    publish_time = Column('publish_time', DateTime)
    sentences = relationship("Sentence")
    publisher_ = relationship(Publisher, lazy='joined')

    def to_dict(self):
        print("publisher", self.publisher, self.publisher_)
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "publisher": self.publisher_.to_dict(),
            "publishTime": self.publish_time.isoformat(),
            "url": self.url,
            "authors": [author for author in self.authors],
            "sentences": [{
                "articleId": sentence.article_id,
                "id": sentence.id,
                "text": sentence.text
            } for sentence in self.sentences]
        }


class Sentence(Base):
    __tablename__ = table_prefix + 'sentence'
    article_id = Column('article_id', Integer, ForeignKey(Article.id), primary_key=True)
    id = Column('id', Integer, primary_key=True)
    text = Column('text', String)

    article = relationship("Article", back_populates="sentences")

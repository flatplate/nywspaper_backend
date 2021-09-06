from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
table_prefix = 'articles_'

class Article(Base):
    __tablename__ = table_prefix + 'article'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String)
    image = Column('image', String)
    publisher = Column('publisher', String)  # TODO maybe use another publisher table
    publish_time = Column('publish_time', DateTime)
    sentences = relationship("Sentence")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "publisher": self.publisher,
            "publishTime": self.publish_time.isoformat(),
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

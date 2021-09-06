from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
table_prefix = 'clusters_'

class Cluster(Base):
    __tablename__ = table_prefix + 'cluster'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String)
    image = Column('image', String)
    importance = Column('importance', Float)
    articles = relationship("Article", lazy="subquery")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'importance': self.importance,
            'articles': [article.id for article in self.articles]
        }

class Article(Base):
    __tablename__ = table_prefix + 'article'
    id = Column('id', Integer, primary_key=True)
    cluster_id = Column('cluster_id', ForeignKey(Cluster.id), nullable=False)

    cluster = relationship("Cluster", back_populates="articles")



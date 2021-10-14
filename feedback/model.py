from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, ARRAY, Float
from sqlalchemy.orm import declarative_base, relationship
import uuid
from datetime import datetime

Base = declarative_base()
table_prefix = 'feedback_'

class Device(Base):
    __tablename__ = table_prefix + 'device'
    uuid = Column('uuid', String, primary_key=True, default=lambda: str(uuid.uuid4()))

    def to_dict(self):
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


class ParagraphFeedback(Base):
    __tablename__ = table_prefix + 'paragraph'
    id = Column('id', Integer, primary_key=True)
    article_one_id = Column('article_one_id', Integer)
    article_two_id = Column('article_two_id', Integer)
    sentence_one_id = Column('sentence_one_id', Integer)
    sentence_two_id = Column('sentence_two_id', Integer)
    similarity = Column('similarity', Float)
    feedback = Column('feedback', Integer)  # Integer to keep it flexible, positive numbers are positive feedback
    uuid = Column('uuid', String, ForeignKey(Device.uuid))
    feedback_time = Column('feedback_time', DateTime, default=datetime.now)

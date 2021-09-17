from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
table_prefix = 'sentences_'

class Sentence(Base):
    __tablename__ = table_prefix + 'sentence'
    id = Column('id', Integer, primary_key=True)
    document_id = Column('document_id', Integer, primary_key=True)
    text = Column('text', String)

    def to_dict(self):
        return {
            "id": self.id,
            "document_id": self.document_id,
            "title": self.title,
        }


class SentenceSimilarity(Base):
    __tablename__ = table_prefix + 'sentence_similarity'
    first_sentence_document_id = Column(
        'first_sentence_document_id',
        primary_key=True
    )
    first_sentence_sentence_id = Column(
        'first_sentence_sentence_id',
        primary_key=True
    )
    second_sentence_document_id = Column(
        'second_sentence_document_id',
        primary_key=True
    )
    second_sentence_sentence_id = Column(
        'second_sentence_sentence_id',
        primary_key=True
    )
    similarity = Column('similarity', Float, nullable=False)

    __table_args__ = (ForeignKeyConstraint([first_sentence_document_id, first_sentence_sentence_id],
                                           [Sentence.document_id, Sentence.id]),
                      ForeignKeyConstraint([second_sentence_document_id, second_sentence_sentence_id],
                                           [Sentence.document_id, Sentence.id]),
                      {})




from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, aliased

from articles.model import Article
from publisher import Publisher
from sentences.model import Sentence, SentenceSimilarity


class SentenceService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_similar_sentences(self, document_id, sentence_id):
        sentence_one = aliased(Sentence)
        sentence_two = aliased(Sentence)

        with Session(self.engine) as session:
            return [{
                "documentId": s2.document_id,
                "id": s2.id,
                "text": s2.text,
                "similarity": sim.similarity,
                "publisher": publisher.to_dict()
            } for s1, s2, sim, article, publisher in session.query(sentence_one, sentence_two, SentenceSimilarity, Article, Publisher).filter(
                SentenceSimilarity.first_sentence_document_id == sentence_one.document_id
            ).filter(
                SentenceSimilarity.first_sentence_sentence_id == sentence_one.id
            ).filter(
                sentence_two.id == SentenceSimilarity.second_sentence_sentence_id
            ).filter(
                sentence_two.document_id == SentenceSimilarity.second_sentence_document_id
            ).filter(
                sentence_one.document_id == document_id
            ).filter(
                sentence_one.id == sentence_id
            ).filter(
                sentence_two.document_id == Article.id
            ).filter(
                Article.publisher == Publisher.id
            ).order_by(SentenceSimilarity.similarity.desc()).all()]

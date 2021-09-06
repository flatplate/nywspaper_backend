
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, aliased

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
                "text": s2.text,
                "similarity": sim.similarity
            } for s1, s2, sim in session.query(sentence_one, sentence_two, SentenceSimilarity).filter(
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
            ).order_by(SentenceSimilarity.similarity.desc()).all()]

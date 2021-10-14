from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from feedback.model import Device, ParagraphFeedback


class FeedbackService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_new_uuid(self):
        with Session(self.engine) as session:
            device = Device()
            session.add(device)
            session.commit()
            uuid = device.uuid
        return uuid

    def insert_paragraph_feedback(
            self,
            article_one_id,
            article_two_id,
            sentence_one_id,
            sentence_two_id,
            similarity,
            feedback,
            uuid
    ):
        with Session(self.engine) as session:
            feedback = ParagraphFeedback(
                article_one_id=article_one_id,
                article_two_id=article_two_id,
                sentence_one_id=sentence_one_id,
                sentence_two_id=sentence_two_id,
                similarity=similarity,
                feedback=feedback,
                uuid=uuid)
            session.add(feedback)
            session.commit()

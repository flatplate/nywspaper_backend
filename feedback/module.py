from flask_restful import Api
from sqlalchemy.engine import Engine

from feedback.model import Base
from feedback.api import Feedback
from feedback.service import FeedbackService


class FeedbackModule:
    def start(self, engine: Engine, api: Api):
        self.update_model(engine)
        service = FeedbackService(engine)
        self.register_endpoint(service, api)

    def register_endpoint(self, service: FeedbackService, api: Api):
        api.add_resource(Feedback, '/api/v1/feedback', resource_class_kwargs={'service': service})

    def update_model(self, engine: Engine):
        Base.metadata.create_all(engine)

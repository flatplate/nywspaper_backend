from flask_restful import Api
from sqlalchemy.engine import Engine

from sentences.model import Base
from sentences.api import SimilarSentences
from sentences.service import SentenceService


class SentenceModule:
    def start(self, engine: Engine, api: Api):
        self.update_model(engine)
        service = SentenceService(engine)
        self.register_endpoint(service, api)

    def register_endpoint(self, service: SentenceService, api: Api):
        api.add_resource(SimilarSentences, '/api/v1/similarsentences', resource_class_kwargs={'service': service})

    def update_model(self, engine: Engine):
        Base.metadata.create_all(engine)

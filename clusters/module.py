from flask_restful import Api
from sqlalchemy.engine import Engine

from clusters.api import Stories
from clusters.model import Base
from clusters.service import StoryService


class ClusterModule:
    def start(self, engine: Engine, api: Api):
        self.update_model(engine)
        service = StoryService(engine)
        self.register_endpoint(service, api)

    def register_endpoint(self, service: StoryService, api: Api):
        api.add_resource(Stories, '/api/v1/stories', resource_class_kwargs={'service': service})

    def update_model(self, engine: Engine):
        Base.metadata.create_all(engine)

from flask_restful import Api
from sqlalchemy.engine import Engine

from articles.api import Articles, ArticleSummary
from articles.service import ArticleService
from articles.model import Base


class ArticleModule:
    def start(self, engine: Engine, api: Api):
        self.update_model(engine)
        service = ArticleService(engine)
        self.register_endpoint(service, api)

    def register_endpoint(self, service: ArticleService, api: Api):
        api.add_resource(ArticleSummary, '/api/v1/articlesummary', resource_class_kwargs={'service': service})
        api.add_resource(Articles, '/api/v1/articles', resource_class_kwargs={'service': service})

    def update_model(self, engine: Engine):
        Base.metadata.create_all(engine)

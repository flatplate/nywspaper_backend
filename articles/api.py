from flask import request
from flask_restful import Resource

from articles.service import ArticleService


class ArticleSummary(Resource):
    def __init__(self, service: ArticleService):
        self.service = service

    def get(self):
        article_ids = request.args.getlist('articles', type=int)
        if not article_ids:
            raise Exception()
        articles = self.service.get_article_summaries(article_ids)
        return articles  # TODO json stuff

class Articles(Resource):
    def __init__(self, service: ArticleService):
        self.service = service

    def get(self):
        article_id = request.args.get('article', type=int)
        if not article_id:
            raise Exception()  # TODO
        article = self.service.get_article(article_id)
        return article  # TODO json stuff

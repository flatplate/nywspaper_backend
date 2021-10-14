from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from flask_cors import CORS

from articles.module import ArticleModule
from clusters.module import ClusterModule
from core.config import get_config
from feedback.module import FeedbackModule
from publisher import Base
from sentences.module import SentenceModule

app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True)

engine = create_engine(get_config()['DATABASE_URL'], echo=True)

Base.metadata.create_all(engine)
ClusterModule().start(engine, api)
ArticleModule().start(engine, api)
SentenceModule().start(engine, api)
FeedbackModule().start(engine, api)

if __name__ == '__main__':
    app.run()

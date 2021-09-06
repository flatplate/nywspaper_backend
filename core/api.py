from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from flask_cors import CORS

from articles.module import ArticleModule
from clusters.module import ClusterModule
from sentences.module import SentenceModule

app = Flask(__name__)
api = Api(app)
CORS(app)

engine = create_engine('postgresql://postgres:123123123u@localhost:5432/postgres', echo=True)

ClusterModule().start(engine, api)
ArticleModule().start(engine, api)
SentenceModule().start(engine, api)

if __name__ == '__main__':
    app.run(debug=True)

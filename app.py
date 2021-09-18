from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from flask_cors import CORS

from articles.module import ArticleModule
from clusters.module import ClusterModule
from core.config import get_config
from load.dataloader import load_data
from publisher import Base
from sentences.module import SentenceModule
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)
api = Api(app)
CORS(app)

engine = create_engine(get_config()['DATABASE_URL'])

Base.metadata.create_all(engine)
ClusterModule().start(engine, api)
ArticleModule().start(engine, api)
SentenceModule().start(engine, api)

load_data()

scheduler = BackgroundScheduler()
scheduler.add_job(func=load_data, trigger="interval", minutes=15)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run()

from sqlalchemy import desc, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from .model import Cluster

class StoryService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_top_stories(self, offset=0):
        with Session(self.engine) as session:
            return [row[0].to_dict() for row in session.execute(select(Cluster).order_by(desc(Cluster.published)).limit(20).offset(offset))]

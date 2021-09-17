from typing import List, Dict, Any

from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from articles.model import Article
from publisher import Publisher


class ArticleService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_article(self, article_id: int) -> dict:
        with Session(self.engine) as session:
            return session.execute(
                select(Article).where(Article.id == article_id)
            ).first()[0].to_dict()

    def get_article_summaries(self, article_ids: List[int]) -> List[Dict[str, Any]]:
        with Session(self.engine) as session:
            return [{
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "publisher": row[3].to_dict(),
                "image": row[4],
                "publishTime": row[5].isoformat(),
            } for row in session.execute(
                select(
                    Article.id,
                    Article.title,
                    Article.description,
                    Publisher,
                    Article.image,
                    Article.publish_time
                ).where(Article.id.in_(article_ids)).filter(Article.publisher == Publisher.id)
            )]

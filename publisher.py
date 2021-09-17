from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)
    logo_url = Column('logo_url', String)
    bias = Column('bias', Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "logo_url": self.logo_url,
            "bias": self.bias
        }
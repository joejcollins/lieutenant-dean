from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INTEGER

Base = declarative_base()
metadata = Base.metadata


class Application(Base):
    __tablename__ = 'application'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(255))

    def __repr__(self):
        return '<Application %r>' % self.name

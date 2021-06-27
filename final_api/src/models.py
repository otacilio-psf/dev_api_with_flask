from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import query, scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///final_api/sprint.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Developers_model(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)
    email = Column(String(80))

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Tasks_model(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(String(40), index=True)
    status = Column(String(40))
    developer_id = Column(Integer, ForeignKey('developers.id'))
    developer = relationship("Developers_model")

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import query, scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///staff.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Developers(Base):
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

class Stacks(Base):
    __tablename__ = 'stacks'
    id = Column(Integer, primary_key=True)
    stack = Column(String(40), index=True)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class DeveloperStack(Base):
    __tablename__ = 'developer_stack'
    id = Column(Integer, primary_key=True)
    developer_id = Column(Integer, ForeignKey('developers.id'))
    developer = relationship("Developers")
    stack_id = Column(Integer, ForeignKey('stacks.id'))
    stack = relationship("Stacks")

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
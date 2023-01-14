import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer,Float,ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class BoardData(Base):
    __tablename__="board"
    board_id =Column(Integer,primary_key=True)
    board_name=Column(String)
    created_date=Column(DateTime,default=datetime.utcnow)
    updated_date=Column(DateTime,default=datetime.utcnow)

class ListItems():
    __tablename__="task_list"
    list_id =Column(Integer,primary_key=True)
    list_name=Column(String)
    board=(String,ForeignKey('Board.id'))
    created_date=Column(DateTime,default=datetime.utcnow)
    updated_date=Column(DateTime,default=datetime.utcnow)

class Taskcard():
    __tablename__="task_items"
    task_id =Column(Integer,primary_key=True)
    card_name=Column(String)
    created_date=Column(DateTime,default=datetime.utcnow)
    updated_date=Column(DateTime,default=datetime.utcnow)
    list=(String,ForeignKey('list.id'))

if __name__ == "__main__":
    engine = create_engine('sqlite:///trolly.sqlite3')
    Base.metadata.create_all(engine)

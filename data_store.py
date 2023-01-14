from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board
    from board_list import BoardList
    from user import User
    from item import Item

from sqlalchemy.orm import sessionmaker
from database_orm import BoardData,ListItems,Taskcard
from sqlalchemy import create_engine
from database_orm import BoardData

class DataStore:
    
    def connect(self):
        engine=create_engine('sqlite:///trolly.sqlite3')
        Session =sessionmaker(bind=engine)
        return Session()

    def add_board(self, model) -> None:
        db = self.connect()
        if isinstance(model, str):
            board = BoardData(board_name = model)
        else:
            board = BoardData(board_name=model.value)
        db.add(board)
        db.commit()
        db.close()

    def get_board(self, id) -> "Board":
        db=self.connect()
        obj=db.query(BoardData).get(id)
        db.close()
        return obj

    def get_boards(self) -> list["Board"]:
        db = self.connect()
        result =db.query(BoardData).all()
        db.close()
        return result

    def update_board(self, model, update):
        raise NotImplementedError

    def remove_board(self, board) -> None:
        db=self.connect()
        print(board)
        db.query(BoardData).filter(BoardData.board_id==board.board_id).delete()
        db.commit()
        db.close()

    def add_user(self, model) -> None:
        raise NotImplementedError

    def get_users(self) -> list["User"]:
        raise NotImplementedError

    def get_user(self, id) -> "User":
        raise NotImplementedError

    def remove_user(self, id) -> None:
        raise NotImplementedError

    def add_list(self, board, model) -> None:
        raise NotImplementedError

    def get_lists(self) -> list["BoardList"]:
        raise NotImplementedError

    def get_list(self, id) -> "BoardList":
        raise []

    def get_lists_by_board(self, board) -> list["BoardList"]:
        return []

    def remove_list(self, board, id) -> None:
        raise NotImplementedError

    def add_item(self, board_list, model) -> None:
        raise NotImplementedError

    def get_items(self, board_list) -> list["Item"]:
        raise NotImplementedError

    def get_item(self, id) -> "Item":
        raise NotImplementedError

    def get_items_by_board(self, board) -> list["Item"]:
        raise NotImplementedError

    def remove_item(self, board_list, id) -> None:
        raise NotImplementedError
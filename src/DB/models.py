from datetime import datetime
from init_db import Connection


class EventCRUD():
    def __init__(self, name):
        self.connection = Connection(name)
        self.cursor = self.connection.cursor

    def create(self, title: str, description: str=None):
        """
        Add a new event to database.
        Params:
        : **kwargs :
            id: int, 
            title: str,
        """
        self.cursor.execute(
            f"INSERT INTO event (title, description, created_at) VALUES (?, ?, ?)",
            (title, description, datetime.now())
            )
        self.connection.close_connect()

    def delete(self, name: str, id: int=None):
        pass
        

if __name__ == "__main__":
    ec = EventCRUD('1.db')
    ec.create(title='new', description='new description')
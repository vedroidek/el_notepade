import sqlite3
from pathlib import Path


class DB:
    """
    Initializing a SQLite database connection.

    Params:
    : path_to_db : str = Absolute or relative path to the file.
    """
    def __init__(self, path_to_db: str) -> None:
        self.path_to_db = path_to_db
        self.conn = sqlite3.Connection
        self.cur = sqlite3.Cursor

    def connect(self) -> bool:
        try:
            self.cur = self.conn.cursor()
            return True
        except sqlite3.Error as err:
            print(f'Error connecting to database: {err}')
            return False
    
    @staticmethod
    def path_to_current_dir():
        return Path.cwd()

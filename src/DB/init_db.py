import sys
from pathlib import Path
import sqlite3

class Connection:
    def __init__(self, name: str) -> None:
        self.db_name = name
        self.path_to_db_file = Path.cwd() / Path(self.name)
        self.connect = sqlite3.connect(self.path_to_db_file, timeout=1.5)
        self.cursor = self.connect.cursor()
        self._create_tables()

    @property
    def name(self):
        if self.db_name[-3:] == '.db':
            return self.db_name
        else:
            self.db_name += '.db'
            return self.db_name
        
    def close_connect(self):
        try:
            self.connect.commit()
        except sqlite3.OperationalError as e:
            self.connect.rollback()
            print("Failed to operation:", e)
        finally:
            self.connect.close()        

    def _create_tables(self):
        try:
            for statement in self.__sql_stmt_list():
                self.cursor.execute(statement)

            self.connect.commit()
            print("Tables created successfully.")

        except sqlite3.OperationalError as e:
            print("Failed to create tables:", e)
            sys.exit(1)

    def __sql_stmt_list(self) -> tuple:
        stmts = (
                '''CREATE TABLE IF NOT EXISTS event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                description TEXT,
                created_at TEXT NOT NULL
                )
                ''',
                '''CREATE TABLE IF NOT EXISTS period (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INT NOT NULL,
                start_at DATE,
                finish_at DATE,
                FOREIGN KEY (event_id) REFERENCES event (id) ON DELETE CASCADE
                )
                '''
        )
        return stmts

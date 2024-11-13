from pathlib import Path
import sqlite3

class Connection:
    def __init__(self, name: str) -> None:
        self._name = name
        self.path_to_db_file = Path.cwd() / Path(self.name)
        self.connect = sqlite3.connect(self.path_to_db_file, timeout=1.5)
        self.cursor = self.connect.cursor()

    @property
    def name(self):
        if self._name[-3:] == '.db':
            return self._name
        else:
            self._name += '.db'
            return self._name

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, *args):
        if exc_type:
            self.connect.rollback()
        else:
            self.connect.commit()
        self.cursor.close()
        self.connect.close()


class CreateTables:
    def __init__(self):
        self.Connect = Connection('1.db')

    def event(self):
        with self.Connect as c:
            c.execute(
                '''CREATE TABLE (?) IF NOT EXISTS event (
                id INTEGER PRIMARY KEY;
                title TEXT NOT NULL;
                '''
                )
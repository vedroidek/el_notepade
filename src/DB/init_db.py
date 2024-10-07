from pathlib import Path
import sqlite3


class Connection:
    def __init__(self, name: str) -> None:
        self._name = name
        self.path_to_db_file = Path.cwd() / Path(self.name)
        self.connect = sqlite3.connect(self.path_to_db_file)
        self.cursor = self.connect.cursor()

    @property
    def name(self, name: str):
        if name[-3:] == '.db':
            return self._name
        else:
            self._name += '.db'
            return self._name


class Session:
    def __init__(self, connect: 'Connection') -> None:
        self.connect = connect.cursor.execute

    def insert(self, table_name: str, *data):
        tmpt = f"INSERT INTO {table_name} VALUES({data})"
        return self.connect(tmpt)

    def get(self, table_name: str, id: int | None, *data):
        tmpt = f'SELECT {data} FROM {table_name}'

    def update(self, table_name: str, id: int | None, **data):
        pass

    def delete(self, table_name: str, id: int | None, **data):
        pass

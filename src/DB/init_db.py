from pathlib import Path
import sqlite3

class Connection:
    def __init__(self, name: str) -> None:
        self._name = name
        self.path_to_db_file = Path.cwd() / Path(self.name)
        self.connect = sqlite3.connect(self.path_to_db_file)
        self.cursor = self.connect.cursor()

    @property
    def name(self):
        if self._name[-3:] == '.db':
            return self._name
        else:
            self._name += '.db'
            return self._name

    def close(self):
        self.connect.close()


class Session:
    def __init__(self, connect: 'Connection') -> None:
        self.connect = connect.cursor

    def insert(self, table_name: str, *data):
        placeholders = ', '.join(['?'] * len(data))
        tmpt = f"INSERT INTO {table_name} (title, description, date, time) VALUES({placeholders})"
        self.connect.execute(tmpt, data)
        self.connect.connection.commit()

    def get(self, table_name: str, id: int | None, *data):
        columns = ', '.join(data) if data else '*'
        tmpt = f'SELECT {columns} FROM {table_name}' + (f' WHERE id = ?' if id is not None else '')
        return self.connect.execute(tmpt, (id,)).fetchall() if id is not None else self.connect.execute(tmpt).fetchall()

    def update(self, table_name: str, id: int | None, **data):
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        tmpt = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        self.connect.execute(tmpt, (*data.values(), id))
        self.connect.connection.commit()

    def delete(self, table_name: str, id: int | None):
        tmpt = f"DELETE FROM {table_name} WHERE id = ?"
        self.connect.execute(tmpt, (id,))
        self.connect.connection.commit()

class EventManager:
    def __init__(self, db_name: str):
        self.connection = Connection(db_name)
        self.session = Session(self.connection)
        self._create_table()

    def _create_table(self):
        """Создает таблицу, если она не существует."""
        self.connection.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL
            )
        ''')
        self.connection.connect.commit()  # Сохраняем изменения

    def create_event(self, title: str, description: str, date: str, time: str):
        """Создает новое событие."""
        self.session.insert('events', title, description, date, time)
        print(f"Событие '{title}' добавлено.")

    def get_events(self):
        """Получает и возвращает все события."""
        events = self.session.get('events', None)  # Получаем все события
        return events

    def update_event(self, event_id: int, title: str, description: str, date: str, time: str):
        """Обновляет данные события по ID."""
        self.session.update('events', event_id, title=title, description=description, date=date, time=time)
        print(f"Событие с ID {event_id} обновлено.")

    def delete_event(self, event_id: int):
        """Удаляет событие по ID."""
        self.session.delete('events', event_id)
        print(f"Событие с ID {event_id} удалено.")

    def close(self):
        """Закрывает соединение с базой данных."""
        self.connection.close()

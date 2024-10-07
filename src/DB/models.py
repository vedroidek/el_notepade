from datetime import date, datetime
from enum import Enum
from typing import NamedTuple
from src.DB.init_db import DBConnect


class Priority(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class TaskModel(NamedTuple):
    task_name: str
    description: str
    created_at: datetime.now
    notification: datetime
    priority: Priority


def create_table(task_name: str,
                 description: str,
                 notification: str):
    """
    Создаёт таблицу 'задача' 
    """
    if conn := (DBConnect.connect()):
        conn.execute(
            """CREATE TABLE IF NOT EXIST task (
            id INTEGER PRIMARY KEY,
            task_name TEXT NOT NULL,
            description TEXT,
            date VARCHAR,
            notification VARCHAR(6),
            )"""
            )
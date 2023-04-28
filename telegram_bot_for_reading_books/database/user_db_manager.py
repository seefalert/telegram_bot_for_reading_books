from typing import List, Dict
import sqlite3

class UserDBManager:
    """
    Класс для управления базой данных пользователей.
    """

    def __init__(self, db_path: str):
        """
        Инициализация менеджера базы данных пользователей.

        Args:
            db_path (str): Путь к файлу базы данных.
        """
        self.db_path = db_path

    def connect(self) -> sqlite3.Connection:
        """
        Создание подключения к базе данных.

        Returns:
            sqlite3.Connection: Объект подключения к базе данных.
        """
        return sqlite3.connect(self.db_path)

    def create_table(self) -> None:
        """
        Создание таблицы пользователей в базе данных.
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            """)

    def add_user(self, name: str, email: str, password: str) -> None:
        """

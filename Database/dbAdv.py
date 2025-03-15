import psycopg2
from psycopg2 import sql
from typing import Optional, Dict

class Database:

    def __init__(self):
            self.conn = psycopg2.connect(
                dbname="test",
                user="postgres",
                password="password",
                host="localhost",
                port=5432
            )
            self.cur = self.conn.cursor()
            self._create_table()
            
    def _create_table(self):
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS advertisements (
                    adv_id BIGINT PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL
                )
            """)
            self.conn.commit()

    def get_advertisement(self, adv_id: int):
        self.cur.execute(
            "SELECT title, description FROM advertisements WHERE adv_id = %s",
            (adv_id,)
        )
        result = self.cur.fetchone()
        if result:
            return {
                "adv_id": adv_id,
                "title": result[0],
                "description": result[1]
            }
        return None

    def save_advertisement(self, data: Dict):
        query = sql.SQL("""
            INSERT INTO advertisements (adv_id, title, description)
            VALUES (%s, %s, %s)
            ON CONFLICT (adv_id) DO UPDATE
            SET title = EXCLUDED.title, description = EXCLUDED.description
        """)
        self.cur.execute(query, (data['adv_id'], data['title'], data['description']))
        self.conn.commit()

    def close(self):
        """Закрыть соединение с базой данных."""
        self.cur.close()
        self.conn.close()
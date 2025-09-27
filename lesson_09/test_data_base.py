from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pytest

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_add_new_column():
	db = create_engine(db_connection_string)
	sql = text("ALTER TABLE customers ADD COLUMN nickname VARCHAR(30)")
	db.execute(sql)


def test_update_column():
	result = db.execute(text("SELECT customer_id FROM customers LIMIT 1"))
	row = result.fetchone()
	assert row is not None, "Таблица пустая, нечего обновлять"
	dynamic_id = row[0]

	sql = text("UPDATE customers SET nickname = :nickname WHERE customer_id = :id")
	db.execute(sql, {"nickname": "cat", "id": dynamic_id})
		
	check = db.execute(text("SELECT nickname FROM customers WHERE customer_id = :id"),
			{"id": dynamic_id}).fetchone()
	assert check[0] == "cat"


def test_drop_column():
	db = create_engine(db_connection_string)
	sql = text("ALTER TABLE customers DROP COLUMN nickname")
	db.execute(sql)

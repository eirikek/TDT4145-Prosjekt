del teater.db
type nul > teater.db
sqlite3 teater.db <  schema.sql
sqlite3 teater.db <  Task1-Task2/insert_data.sql
python Task1-Task2/insert_chairs.py
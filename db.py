import sqlite3

# scripts for database
CREATE_USER = '''
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
'''

CREATE_MEMO = '''
CREATE TABLE MEMO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''

def create_table(cursor, table_name, script):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    is_exist = cursor.fetchone()
    if (is_exist):
        print(f'{table_name} database is already exits')
    else:
        cursor.execute(script)

# crate database
con = sqlite3.connect('database.db')

# make cursor to manipulate database
cursor = con.cursor()

# create database
create_table(cursor, 'USER', CREATE_USER)
create_table(cursor, 'MEMO', CREATE_MEMO)

# save changes
con.commit()

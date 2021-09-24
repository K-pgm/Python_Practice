import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

create_user_table_query = """
CREATE TABLE IF NOT EXISTS User (
    UserId INTEGER PRIMARY KEY NOT NULL,
    NAME TEXT DEFAULT 'anonymous',
    Email TEXT NOT NULL,
    Age INTEGER CHECK(Age > 0)
)
"""

cursor.execute(create_user_table_query)

insert_user_query = """
INSERT INTO USer VALUES(1, 'John', 'john@gmail.com', 30);
INSERT INTO USer VALUES(2, 'Emily', 'Emily@gmail.com', 28);
INSERT INTO USer VALUES(3, 'Taro', 'Taro@gmail.com', 25);
"""
cursor.executescript(insert_user_query)
con.commit()

import sqlite3

conn = sqlite3.connect('user_db.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE experiments (id VARCHAR, name VARCHAR)')
conn.commit()
conn.close()
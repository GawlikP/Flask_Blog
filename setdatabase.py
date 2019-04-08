import sqlite3

conn = sqlite3.connect('dbase.db')

conn.execute('CREATE TABLE post (title TEXT, content TEXT)')

conn.execute('CREATE TABLE user (name TEXT, password TEXT)')

print("Write admin username:")
username = str(input())
print("Write admin password")
password = str(input())
conn.execute('INSERT INTO user (name, password) VALUES (?,?)',(username,password))
conn.commit()

conn.close()
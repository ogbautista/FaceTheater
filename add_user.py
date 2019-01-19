import sqlite3

#Open or Creates de database file
conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()

#Creates the table "Users" with 3 fields
cur.execute('''CREATE TABLE IF NOT EXISTS Users
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, memberId TEXT UNIQUE)''')

name = input("Name: ").upper()
mId = input("Member ID: ").upper()

cur.execute('INSERT OR IGNORE INTO Users (name, memberId) VALUES ( ?, ? )', ( name, mId ) )

conn.commit()
cur.close()

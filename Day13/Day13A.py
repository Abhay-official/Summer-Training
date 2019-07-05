import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()
cur.execute( 'select SQLITE_VERSION()')

data = cur.fetchone()
print(data)

import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute( 'select SQLITE_VERSION()')

data = cur.fetchone()
print(data)


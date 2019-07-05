
import sqlite3 as lite
con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute('''CREATE TABLE Cars(Id INT, Name TEXT, Price INT)''')
    print("Table cars created")
    cur.execute("INSERT INTO Cars Values(1, 'Audi', 52642)")
    cur.execute("INSERT INTO Cars Values(2, 'Mercedes', 57125)")
print("Data inserted successfully")

import sqlite3 as lite

Cars = (
    (1, 'Audi',52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley',350000),
    (6, 'Hammer', 41400),
    (7, 'Volkswagen', 21600)
    )

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?,?,?)", Cars)


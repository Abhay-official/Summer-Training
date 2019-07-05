import sqlite3 as lite
con = lite.connect("test.db")

with con:
    cur = con.cursor()
    cur.execute("Select * from data1")
    rows = cur.fetchall()

print("-"*20)
for row in rows:
    print(row)


with con:
    cur = con.cursor()
    cur.execute("Select * from data2")
    rows = cur.fetchall()

print("-"*20)
for row in rows:
    print(row)

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


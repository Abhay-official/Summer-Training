import sqlite3 as lite
con = lite.connect("Test.db")

with con:
    cur = con.cursor()
    cur.execute("Select * from cars")
    rows = cur.fetchall()

print(rows)
print("-"*20)
for row in rows:
    print(row)

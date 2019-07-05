import sqlite3 as lite

cars = (
    (1,"Audi",67589),
    (2,"Hero Honda",6759),
    (3,"Honda",6789),
    (4,"GT",6758),
    (5,"Hummer",7589),
    (6,"Shoda",62589),
    (7,"Valca",589) )

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute('CREATE TABLE Cars(Id INT, Name TEXT, Price INT)')
    cur.executemany("INSERT INTO Cars Values(?,?,?)",cars)
print("Data inserted successfully")

import sqlite3 as lite
import sys
try:
    con = lite.connect('test.db')
    cur = con.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
        INSERT INTO Cars values(6, 'Citroen', 21000);
        INSERT INTO Cars values(7, 'Hummer', 43000);
        INSERT INTO Cars values(8, 'Volkswagen', 21600);
    """)
    con.commit()
except lite.Error as e:
    if e:
        con.rollback()
        print("Error %s"% e.args[0])
        sys.exit()
finally:
    if con:
        con.close()
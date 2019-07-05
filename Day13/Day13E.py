import sqlite3 as lite
con = lite.connect('test.db')

def input_fun():
    a = int(input('Enter ID: '))
    b = input('Enter name: ')
    b = "'" + b + "'"
    c = int(input("Enter Price:"))
    str1 = "INSERT INTO Cars VALUES({}, {}, {})".format(a, b, c)
    return str1

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    print("Table cars created")
    cur.execute(input_fun())

print("Values in table cars inserted")

import sqlite3 as lite
con = lite.connect('test.db')

def input_fun():
    a = int(input('Enter ID: '))
    b = input('Enter name: ')
    b = "'" + b + "'"
    c = int(input("Enter Price:"))
    str1 = "INSERT INTO Cars VALUES({}, {}, {})".format(a, b, c)
    return str1

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    print("Table cars created")
    cur.execute(input_fun())

print("Values in table cars inserted")
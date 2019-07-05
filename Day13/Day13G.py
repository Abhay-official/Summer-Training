import random
import sqlite3 as lite

def str_float(x):
    for i in range(0,len(x)-1):
        x[i] = float(x[i])
    return tuple(x)

data1 = []
data2 = []
for line in open("iris.txt"):
    temp = line[:-1].split(",") if line[-1]=="\n" else line.split(",")
    if random.random() <= 0.8:
        data1.append(str_float(temp))
    else:
        data2.append(str_float(temp))

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS DATA1")
    cur.execute("DROP TABLE IF EXISTS DATA2")
    cur.execute('CREATE TABLE DATA1(x1 INT, y1 INT,  x2 INT,  y2 INT, Name TEXT)')
    cur.execute('CREATE TABLE DATA2(x1 INT, y1 INT,  x2 INT,  y2 INT, Name TEXT)')
    cur.executemany("INSERT INTO DATA1 Values(?,?,?,?,?)",data1)
    cur.executemany("INSERT INTO DATA2 Values(?,?,?,?,?)",data2)
print("Data inserted successfully")

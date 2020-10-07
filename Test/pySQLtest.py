#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="YOURDBNAME", user = "YOURUSER", password = "YOURPASSWORD", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

# CREATE TABLE
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')
# print("Table created successfully")

# INSERTING
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# conn.commit()  USED FOR CREATION OF TABLE AND INSERTING

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()

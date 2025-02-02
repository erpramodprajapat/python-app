import sqlite3

# Data access layer, function to perform to CURD on DB
#custom module

# code first approach
# DB first approch
from emp import Emp

def connectDB():
    global conn
    conn=sqlite3.connect("C:\\py-tt\\Day-03\\database\\employees.db")
    global cursor
    cursor=conn.cursor
    print("connected to database")

def createTable():
    pass

def insertEmp(emp):
    pass

def readEmp(Emp):
    pass

def deleteEmp(Emp):
    pass

#Test Code
print("working with SQLLite3")
connectDB()


import pymysql
from tkinter import *
import tkinter.messagebox

#db connection
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "db_test"
)

def productRegistration(rt, v1, v2, v3, v4, v5, v6, v7):
    #cursor initialization
    cursor = db.cursor()

    #table used
    cursor.execute("USE Table1")

    #variables
    id = v1.get()
    pc = v2.get()
    pa = v3.get()
    pv = v4.get()
    pf = v5.get()
    data = v6.get()
    status = v7.get()

    try:
        sql = ("INSERT INTO db_test (id, pc, pa, pv, pf, data, status) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        val = (id, pc, pa, pv, pf, data, status)

        cursor.execute(sql, val)
        db.commit()
        tkinter.messagebox.showinfo('Success', "Product added succesfully!")
        rt.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")
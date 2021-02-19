
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




import mysql.connector  #pip install mysql-connector-python
from tkinter import *
import tkinter.messagebox

# db connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "db_test",
    auth_plugin='mysql_native_password'
)

# commands
def productRegistration():
    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    # variables
    id = str(prod1.get())
    pc = prod2.get()
    pa = prod3.get()
    pv = prod4.get()
    pf = prod5.get()
    data = str(prod6.get())
    status = str(prod7.get())

    # insert
    try:
        sql = "INSERT INTO Table2 VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (id, pc, pa, pv, pf, data, status)

        cursor.execute(sql, val)
        db.commit()

        tkinter.messagebox.showinfo('Success', "Product added successfully!")
        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def productElimination():
    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    # variables
    id = str(prod1.get())

    # insert
    try:
        sql = "DELETE FROM Table2 WHERE id = %s"
        val = (id)

        cursor.execute(sql, val)
        db.commit()

        tkinter.messagebox.showinfo('Success', "Product deleted successfully!")
        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def upStat():
    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    # variables
    id = str(prod1.get())
    status = str(prod2.get())

    try:
        sql = ("UPDATE Table2 SET status = %s WHERE id = %s ")
        val = (status, id)

        cursor.execute(sql, val)
        db.commit()

        tkinter.messagebox.showinfo('Success', "Product status updated successfully!")
        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def deleteSold():
    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    try:
        sql = ("DELETE FROM Table2 WHERE status = 'sold'")

        cursor.execute(sql)
        db.commit()
        tkinter.messagebox.showinfo('Succcess!', "Successfully deleted all sold items!")
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def showPending():
    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    try:
        sql = ("SELECT * FROM Table2 WHERE status = 'pending'")

        cursor.execute(sql)

        my_w = tkinter.Tk()
        my_w.geometry("450x150")

        i = 0
        for x in cursor:
            for j in range(len(x)):
                e = Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, x[j])
            i = i + 1

    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def showStock():
    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    try:
        sql = ("SELECT * FROM Table2")

        cursor.execute(sql)

        my_w = tkinter.Tk()
        my_w.geometry("450x150")

        i = 0
        for x in cursor:
            for j in range(len(x)):
                e = Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, x[j])
            i = i + 1

    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

#operations
def addProd():
    global root2, prod1, prod2, prod3, prod4, prod5, prod6, prod7, labelframe

    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    # addProd window
    root2 = Toplevel(root)
    root2.title("Add Product")
    root2.minsize(width = 400, height = 400)
    root2.geometry("700x700")
    root2.config(bg = "#99ccff")

    # header
    head2 = Frame(root2, bg = "#0080ff", bd = 5)
    head2.place(relx = 0.25, rely = 0.2, relwidth = 0.5, relheight = 0.08)

    head2_label = Label(head2, text = "Add Product", bg = 'black', fg = 'white', font = ('Courier', 15))
    head2_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    # variable frame
    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.3)

    # id
    lb1 = Label(labelFrame, text="ID: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.1, relheight=0.08)

    prod1 = Entry(labelFrame)
    prod1.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # pc
    lb2 = Label(labelFrame, text="PC: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.25, relheight=0.08)

    prod2 = Entry(labelFrame)
    prod2.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # pa
    lb3 = Label(labelFrame, text="PA: ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.4, relheight=0.08)

    prod3 = Entry(labelFrame)
    prod3.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)

    # pv
    lb4 = Label(labelFrame, text="PV: ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.55, relheight=0.08)

    prod4 = Entry(labelFrame)
    prod4.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    # pf
    lb5 = Label(labelFrame, text="PF: ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)

    prod5 = Entry(labelFrame)
    prod5.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.08)

    # data
    lb6 = Label(labelFrame, text="DATA: ", bg='black', fg='white')
    lb6.place(relx=0.05, rely=0.85, relheight=0.08)

    prod6 = Entry(labelFrame)
    prod6.place(relx=0.3, rely=0.85, relwidth=0.62, relheight=0.08)

    # status
    lb7 = Label(labelFrame, text="STATUS: ", bg='black', fg='white')
    lb7.place(relx=0.05, rely=1, relheight=0.08)

    prod7 = Entry(labelFrame)
    prod7.place(relx=0.3, rely=1, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text = "SUBMIT", bg = '#d1ccc0', fg = 'black', command = productRegistration)
    submitbut.place(relx = 0.28, rely = 0.8, relwidth = 0.18, relheight = 0.08)

    # cancel
    cancelbut = Button(root2, text = "Quit", bg = '#f7f1e3', fg = 'black', command = root2.destroy)
    cancelbut.place(relx = 0.53, rely = 0.8, relwidth = 0.18, relheight = 0.08)

    root2.mainloop()

def delProd():
    global root2, prod1, labelframe

    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    # delProd window
    root2 = Toplevel(root)
    root2.title("Delete Product")
    root2.minsize(width=400, height=400)
    root2.geometry("700x700")
    root2.config(bg="#99ccff")

    # header
    head2 = Frame(root2, bg="#0080ff", bd=5)
    head2.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.08)

    head2_label = Label(head2, text="Delete Product", bg='black', fg='white', font=('Courier', 15))
    head2_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # variable frame
    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)

    # id
    lb1 = Label(labelFrame, text="ID: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.3, relheight=0.2)

    prod1 = Entry(labelFrame)
    prod1.place(relx=0.3, rely=0.3, relwidth=0.6, relheight=0.3)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=productElimination)
    submitbut.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def updateStatus():
    global root2, prod1, prod2, labelframe

    # cursor initialization
    cursor = db.cursor()

    # db used
    cursor.execute("USE db_test")

    # upStat window
    root2 = Toplevel(root)
    root2.title("Update Status")
    root2.minsize(width=400, height=400)
    root2.geometry("700x700")
    root2.config(bg="#99ccff")

    # header
    head2 = Frame(root2, bg="#0080ff", bd=5)
    head2.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.08)

    head2_label = Label(head2, text="Update Status", bg='black', fg='white', font=('Courier', 15))
    head2_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # variable frame
    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)

    # id
    lb1 = Label(labelFrame, text="ID: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.2)

    prod1 = Entry(labelFrame)
    prod1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.2)

    # updated status
    lb2 = Label(labelFrame, text="Updated Status: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.6, relheight=0.2)

    prod2 = Entry(labelFrame)
    prod2.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.2)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=upStat)
    submitbut.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root2.mainloop()

#main
def main():
    global root

    # main window
    root = Tk()
    root.title("Serenity Vintage")
    root.minsize(width = 700, height = 700)
    root.geometry("700x700")
    root.config(bg = "#99ccff")

    # head
    head1 = Frame(root, bg = "#0080ff", bd = 5)
    head1.place(relx = 0.2, rely = 0.1, relwidth = 0.6, relheight = 0.15)
    head1Label = Label(head1, text = "Welcome to \n Serenity Vintage Database", bg = 'black', fg = 'white', font = ('Courier', 15))
    head1Label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    # op buttons
    b1 = Button(root, text = "Add Product", bg = 'black', fg = 'white', command = lambda: addProd())
    b1.place(relx = 0.1, rely = 0.4, relwidth = 0.30, relheight = 0.1)

    b2 = Button(root, text="Show Stock", bg='black', fg='white', command=lambda:showStock())
    b2.place(relx=0.6, rely=0.4, relwidth=0.30, relheight=0.1)

    b3 = Button(root, text="Delete Product", bg='black', fg='white', command=lambda: delProd())
    b3.place(relx=0.1, rely=0.5, relwidth=0.30, relheight=0.1)

    b4 = Button(root, text="Delete Sold", bg='black', fg='white', command=lambda: deleteSold())
    b4.place(relx=0.6, rely=0.5, relwidth=0.30, relheight=0.1)

    b5 = Button(root, text="Show Pending", bg='black', fg='white', command=lambda: showPending())
    b5.place(relx=0.1, rely=0.6, relwidth=0.30, relheight=0.1)

    b6 = Button(root, text="Update Status", bg='black', fg='white', command=lambda: updateStatus())
    b6.place(relx=0.6, rely=0.6, relwidth=0.30, relheight=0.1)

    root.mainloop()

main()

#close db connection
db.close()

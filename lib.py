#libraries

import mysql.connector
from tkinter import *
import tkinter.messagebox

#db connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

#functions

def userRegistration():
    #cursor initialization
    cursor = db.cursor()

    #specify table used
    cursor.execute("USE test2")

    #variables
    name = user1.get()
    address = user2.get()
    try:
        sql = ("INSERT INTO users2 (name, address) VALUES (%s, %s)")
        val = (name, address)

        cursor.execute(sql, val)
        db.commit()
        tkinter.messagebox.showinfo('Success', "User added succesfully!")
        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def bookRegistration():
    #cursor initialization
    cursor = db.cursor()

    #specify db used
    cursor.execute("USE test2")

    #variables
    title = book1.get()
    author = book2.get()
    noc = book3.get()
    nocl = 0
    try:
        sql = ("INSERT INTO books2 (title, author, noc, nocl) VALUES (%s, %s, %s, %s)")
        val = (title, author, noc, nocl)

        cursor.execute(sql, val)
        db.commit()
        tkinter.messagebox.showinfo('Success', "Book added successfully!")
        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def deleteAcc():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    name = user1.get()
    try:
        sql = ("DELETE FROM users2 WHERE name = %s")
        val = name

        cursor.execute(sql, (val,))
        db.commit()
        tkinter.messagebox.showinfo('Success', "User deleted succesfully!")

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def userUpdate():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    name = user1.get()
    address = user2.get()
    try:
        sql = ("UPDATE users2 SET address = %s WHERE name = %s")
        val = (address, name)

        cursor.execute(sql, val)
        db.commit()
        tkinter.messagebox.showinfo('Success', "User information updated succesfully!")

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def showAcc():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    name = user1.get()
    try:
        l = ""
        sql = ("SELECT * FROM users2 WHERE name = %s")
        val = name

        cursor.execute(sql, (val,))
        for x in cursor:
            l = l + str(x)
        db.commit()
        tkinter.messagebox.showinfo('Success', l)

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def delBook():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    title = book1.get()
    author = book2.get()

    #author = book2.get()

    try:
        sql = ("DELETE FROM books2 WHERE title = %s AND author = %s")
        val = (title, author)

        cursor.execute(sql, val)
        db.commit()
        tkinter.messagebox.showinfo('Success', "Book deleted succesfully!")

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def upBook():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    title = book1.get()
    author = book2.get()
    noc = book3.get()

    try:
        sql = ("UPDATE books2 SET noc = %s WHERE title = %s AND author = %s")
        val = (noc, title, author)

        cursor.execute(sql, val)
        db.commit()
        tkinter.messagebox.showinfo('Success', "Book updated succesfully!")

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def shBook():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    title = book1.get()
    author = book2.get()

    if len(title) != 0 and len(author) != 0:
        try:
            sql = ("SELECT * FROM books2 WHERE title = %s AND author = %s")
            val = (title, author)

            cursor.execute(sql, val)

            my_w = tkinter.Tk()
            my_w.geometry("400x250")

            i = 0
            for x in cursor:
                for j in range(len(x)):
                    e = Entry(my_w, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            db.commit()

            root2.destroy()
        except:
            tkinter.messagebox.showinfo('Failed', "Operation failed!")
    elif len(title) != 0 and len(author) == 0:
        try:
            sql = ("SELECT * FROM books2 WHERE title = %s")
            val = title

            cursor.execute(sql, (val,))

            my_w = tkinter.Tk()
            my_w.geometry("400x250")

            i = 0
            for x in cursor:
                for j in range(len(x)):
                    e = Entry(my_w, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            db.commit()

            root2.destroy()
        except:
            tkinter.messagebox.showinfo('Failed', "Operation failed!")

    if len(title) == 0 and len(author) != 0:
        try:
            sql = ("SELECT * FROM books2 WHERE author = %s")
            val = author

            cursor.execute(sql, (val, ))

            my_w = tkinter.Tk()
            my_w.geometry("400x250")
            i = 0
            for x in cursor:
                for j in range(len(x)):
                    e = Entry(my_w, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            db.commit()

            root2.destroy()
        except:
            tkinter.messagebox.showinfo('Failed', "Operation failed!")

def loan():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # variables
    name = user1.get()
    title = book1.get()
    author = book2.get()

    try:
        #insert loan
        sql = ("INSERT INTO loan2 (title, author, user) VALUES (%s, %s, %s)")
        val = (title, author, name)

        cursor.execute(sql, val)

        #update bookstable
        sql = ("UPDATE books2 SET nocl = nocl + 1 WHERE title = %s AND author = %s")
        val = (title, author)

        cursor.execute(sql, val)

        db.commit()
        tkinter.messagebox.showinfo('Success', "Book loaned succesfully!")

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

#button functions USER

def addUser():

    global user1, user2, user3, labelFrame, root2

    #cursor initialization
    cursor = db.cursor()

    #specify table used
    cursor.execute("USE test2")

    #creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")

    #canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    #can1.pack(expand=True, fill=BOTH)
    can1.pack()

    #heading
    head2 = Frame(root2,bg="#FFBB00",bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Add User", bg='black', fg='white', font=('Courier',15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #name
    lb1 = Label(labelFrame,text="Name: ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    user1 = Entry(labelFrame)
    user1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    #address
    lb2 = Label(labelFrame, text="Address: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    user2 = Entry(labelFrame)
    user2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    #submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=userRegistration)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def deleteUser():

    global user1, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")
    cursor = db.cursor()
    cursor.execute("USE test2")

    #canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    #can1.pack(expand=True, fill=BOTH)
    can1.pack()

    #heading
    head2 = Frame(root2,bg="#FFBB00",bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Delete User", bg='black', fg='white', font=('Courier',15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # name
    lb1 = Label(labelFrame, text="User Name: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    user1 = Entry(labelFrame)
    user1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteAcc)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def updateAddress():
    global user1, user2, user3, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width = 400, height = 400)
    root2.geometry("600x500")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg = "#ff6e40")
    # can1.pack(expand = True, fill = BOTH)
    can1.pack()

    # heading
    head2 = Frame(root2, bg = "#FFBB00", bd = 5)
    head2.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    head2Label = Label(head2, text = "Update User", bg = 'black', fg = 'white', font = ('Courier', 15))
    head2Label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    labelFrame = Frame(root2, bg = 'black')
    labelFrame.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.4)

    # name
    lb1 = Label(labelFrame, text = "User Name: ", bg = 'black', fg = 'white')
    lb1.place(relx = 0.05, rely = 0.2, relheight = 0.08)

    user1 = Entry(labelFrame)
    user1.place(relx = 0.3, rely = 0.2, relwidth = 0.62, relheight = 0.08)

    # address
    lb2 = Label(labelFrame, text = "Address: ", bg = 'black', fg = 'white')
    lb2.place(relx = 0.05, rely = 0.35, relheight = 0.08)

    user2 = Entry(labelFrame)
    user2.place(relx = 0.3, rely = 0.35, relwidth = 0.62, relheight = 0.08)

    # submit
    submitbut = Button(root2, text = "SUBMIT", bg = '#d1ccc0', fg = 'black', command = userUpdate)
    submitbut.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    # cancel
    cancelbut = Button(root2, text = "Quit", bg = '#f7f1e3', fg = 'black', command = root2.destroy)
    cancelbut.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    root2.mainloop()

def showUser():
    global user1, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width = 400, height = 400)
    root2.geometry("600x500")
    cursor = db.cursor()
    cursor.execute("USE test2")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg = "#ff6e40")
    can1.pack()

    # heading
    head2 = Frame(root2, bg = "#FFBB00", bd = 5)
    head2.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    head2Label = Label(head2, text = "Show user information", bg = 'black', fg = 'white', font = ('Courier', 15))
    head2Label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    labelFrame = Frame(root2, bg = 'black')
    labelFrame.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.4)

    # name
    lb1 = Label(labelFrame, text = "User Name: ", bg = 'black', fg = 'white')
    lb1.place(relx = 0.05, rely = 0.2, relheight = 0.08)

    user1 = Entry(labelFrame)
    user1.place(relx = 0.3, rely = 0.2, relwidth = 0.62, relheight = 0.08)

    # submit
    submitbut = Button(root2, text = "SUBMIT", bg = '#d1ccc0', fg = 'black', command = showAcc)
    submitbut.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    # cancel
    cancelbut = Button(root2, text = "Quit", bg = '#f7f1e3', fg = 'black', command = root2.destroy)
    cancelbut.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    root2.mainloop()

def userTable():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    try:
        sql = ("SELECT * FROM users2")

        cursor.execute(sql)

        my_w = tkinter.Tk()
        my_w.geometry("200x100")

        i = 0
        for x in cursor:
            for j in range(len(x)):
                e = Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, x[j])
            i = i + 1

        db.commit()

        # root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def main():
    global root

    # main window
    root = Tk()
    root.title("Library Management")
    root.minsize(width = 500, height = 500)
    root.geometry("500x500")

    # head
    head1 = Frame(root, bg = "#FFBB00", bd = 5)
    head1.place(relx = 0.2, rely = 0.1, relwidth = 0.6, relheight = 0.16)
    head1Label = Label(head1, text = "Welcome to \n <name> Library", bg = 'black', fg = 'white', font = ('Courier', 15))
    head1Label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    # op buttons
    b1 = Button(root, text = "Add User", bg = 'black', fg = 'white', command = lambda: addUser())
    b1.place(relx = 0.2, rely = 0.4, relwidth = 0.30, relheight = 0.1)

    b2 = Button(root, text = "Delete User", bg = 'black', fg = 'white', command = lambda: deleteUser())
    b2.place(relx = 0.2, rely = 0.5, relwidth = 0.30, relheight = 0.1)

    b3 = Button(root, text = "Update User", bg = 'black', fg = 'white', command = lambda: updateAddress())
    b3.place(relx = 0.2, rely = 0.6, relwidth = 0.30, relheight = 0.1)

    b4 = Button(root, text = "Show User", bg = 'black', fg = 'white', command = lambda: showUser())
    b4.place(relx = 0.2, rely = 0.7, relwidth = 0.30, relheight = 0.1)

    b5 = Button(root, text = "Add Book", bg = 'black', fg = 'white', command = lambda: addBook())
    b5.place(relx = 0.5, rely=0.4, relwidth = 0.30, relheight = 0.1)

    b6 = Button(root, text = "Delete Book", bg = 'black', fg = 'white', command = lambda: deleteBook())
    b6.place(relx = 0.5, rely = 0.5, relwidth = 0.30, relheight = 0.1)

    b7 = Button(root, text = "Update Book", bg = 'black', fg = 'white', command = lambda: updateBook())
    b7.place(relx = 0.5, rely = 0.6, relwidth = 0.30, relheight = 0.1)

    b8 = Button(root, text = "Show Book", bg = 'black', fg = 'white', command = lambda: showBook())
    b8.place(relx = 0.5, rely = 0.7, relwidth = 0.30, relheight = 0.1)

    b8 = Button(root, text="User Table", bg='black', fg='white', command=lambda: userTable())
    b8.place(relx=0.2, rely=0.8, relwidth=0.30, relheight=0.1)

    b9 = Button(root, text="Book Table", bg='black', fg='white', command=lambda: bookTable())
    b9.place(relx=0.5, rely=0.8, relwidth=0.30, relheight=0.1)

    b10 = Button(root, text="Loan Book", bg='black', fg='white', command=lambda: loanBook())
    b10.place(relx=0.2, rely=0.9, relwidth=0.30, relheight=0.1)

    b11 = Button(root, text="Show Loans", bg='black', fg='white', command=lambda: loanTable())
    b11.place(relx=0.5, rely=0.9, relwidth=0.30, relheight=0.1)

    b12 = Button(root, text="Return Book", bg='black', fg='white', command=lambda: returnBook())
    b12.place(relx=0.5, rely=0.10, relwidth=0.30, relheight=0.1)

    root.mainloop()

#button functions books

def addBook():

    global book1, book2, book3, labelFrame, root2

    #cursor initialization
    cursor = db.cursor()

    #specify table used
    cursor.execute("USE test2")

    #creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width = 400, height=400)
    root2.geometry("600x500")

    #canvas
    can1 = Canvas(root2)

    can1.config(bg = "#ff6e40")
    can1.pack()

    #heading
    head2 = Frame(root2, bg = "#FFBB00", bd = 5)
    head2.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    head2Label = Label(head2, text = "Add Book", bg = 'black', fg = 'white', font = ('Courier', 15))
    head2Label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    labelFrame = Frame(root2, bg = 'black')
    labelFrame.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.4)

    #title
    lb1 = Label(labelFrame, text = "Title: ", bg = 'black', fg = 'white')
    lb1.place(relx = 0.05, rely = 0.2, relheight = 0.08)

    book1 = Entry(labelFrame)
    book1.place(relx = 0.3, rely = 0.2, relwidth = 0.62, relheight = 0.08)

    #Author
    lb2 = Label(labelFrame, text = "Author: ", bg = 'black', fg = 'white')
    lb2.place(relx = 0.05, rely = 0.35, relheight = 0.08)

    book2 = Entry(labelFrame)
    book2.place(relx = 0.3, rely = 0.35, relwidth = 0.62, relheight = 0.08)

    #Number of copies
    lb3 = Label(labelFrame, text = "Number of copies: ", bg = 'black', fg = 'white')
    lb3.place(relx = 0.05, rely = 0.5, relheight = 0.08)

    book3 = Entry(labelFrame)
    book3.place(relx = 0.3, rely = 0.5, relwidth = 0.62, relheight = 0.08)

    #submit
    submitbut = Button(root2, text = "SUBMIT", bg = '#d1ccc0', fg = 'black', command = bookRegistration)
    submitbut.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    #cancel
    cancelbut = Button(root2, text = "Quit", bg = '#f7f1e3', fg = 'black', command = root2.destroy)
    cancelbut.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight=0.08)

    root2.mainloop()

def deleteBook():
    global book1, book2, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    # can1.pack(expand = True, fill = BOTH)
    can1.pack()

    # heading
    head2 = Frame(root2, bg="#FFBB00", bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # name
    lb1 = Label(labelFrame, text="Title: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    book1 = Entry(labelFrame)
    book1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # address
    lb2 = Label(labelFrame, text="Author: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    book2 = Entry(labelFrame)
    book2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=delBook)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def updateBook():
    global book1, book2, book3, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    # can1.pack(expand = True, fill = BOTH)
    can1.pack()

    # heading
    head2 = Frame(root2, bg="#FFBB00", bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Update Book", bg='black', fg='white', font=('Courier', 15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # name
    lb1 = Label(labelFrame, text="Title: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    book1 = Entry(labelFrame)
    book1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # address
    lb2 = Label(labelFrame, text="Author: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    book2 = Entry(labelFrame)
    book2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # address
    lb2 = Label(labelFrame, text="Number of Copies: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5, relheight=0.08)

    book3 = Entry(labelFrame)
    book3.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=upBook)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def showBook():
    global book1, book2, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    # can1.pack(expand = True, fill = BOTH)
    can1.pack()

    # heading
    head2 = Frame(root2, bg="#FFBB00", bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Show Book", bg='black', fg='white', font=('Courier', 15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # name
    lb1 = Label(labelFrame, text="Title: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    book1 = Entry(labelFrame)
    book1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # address
    lb2 = Label(labelFrame, text="Author: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    book2 = Entry(labelFrame)
    book2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=shBook)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def bookTable():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    try:
        sql = ("SELECT * FROM books2")

        cursor.execute(sql)

        my_w = tkinter.Tk()
        my_w.geometry("400x250")

        i = 0
        for x in cursor:
            for j in range(len(x)):
                e = Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, x[j])
            i = i + 1

        db.commit()

        #root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

#loan book function

def loanBook():
    global user1, book1, book2, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")
    cursor = db.cursor()
    cursor.execute("USE test2")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    can1.pack()

    # heading
    head2 = Frame(root2, bg="#FFBB00", bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Loan Book", bg='black', fg='white', font=('Courier', 15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # name
    lb1 = Label(labelFrame, text="User Name: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    user1 = Entry(labelFrame)
    user1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    #title
    lb1 = Label(labelFrame, text="Book Title: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.35, relheight=0.08)

    book1 = Entry(labelFrame)
    book1.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #author
    lb1 = Label(labelFrame, text="Book Author: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5, relheight=0.08)

    book2 = Entry(labelFrame)
    book2.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=loan)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def loanTable():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    try:
        sql = ("SELECT * FROM loan2")

        cursor.execute(sql)

        my_w = tkinter.Tk()
        my_w.geometry("500x250")

        i = 0
        for x in cursor:
            for j in range(len(x)):
                e = Entry(my_w, width=20, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, x[j])
            i = i + 1

        db.commit()

        # root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

def returnBook():
    global user1, book1, book2, labelFrame, root2

    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    # creating the addUser window
    root2 = Toplevel(root)
    root2.title("Library Management")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")
    cursor = db.cursor()
    cursor.execute("USE test2")

    # canvas
    can1 = Canvas(root2)

    can1.config(bg="#ff6e40")
    can1.pack()

    # heading
    head2 = Frame(root2, bg="#FFBB00", bd=5)
    head2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    head2Label = Label(head2, text="Loan Book", bg='black', fg='white', font=('Courier', 15))
    head2Label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # name
    lb1 = Label(labelFrame, text="User Name: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    user1 = Entry(labelFrame)
    user1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # title
    lb1 = Label(labelFrame, text="Book Title: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.35, relheight=0.08)

    book1 = Entry(labelFrame)
    book1.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # author
    lb1 = Label(labelFrame, text="Book Author: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5, relheight=0.08)

    book2 = Entry(labelFrame)
    book2.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # submit
    submitbut = Button(root2, text="SUBMIT", bg='#d1ccc0', fg='black', command=ret)
    submitbut.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # cancel
    cancelbut = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    cancelbut.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def ret():
    # cursor initialization
    cursor = db.cursor()

    # specify table used
    cursor.execute("USE test2")

    name = user1.get()
    title = book1.get()
    author = book2.get()

    try:
        # insert loan
        sql = ("DELETE FROM loan2 WHERE name = %s AND title = %s AND author = %s)")
        val = (name, title, author,)

        cursor.execute(sql, val)

        # update bookstable
        sql = ("UPDATE books2 SET nocl = nocl - 1 WHERE title = %s AND author = %s")
        val = (title, author)

        cursor.execute(sql, val)

        db.commit()
        tkinter.messagebox.showinfo('Success', "Book returned succesfully!")

        root2.destroy()
    except:
        tkinter.messagebox.showinfo('Failed', "Operation failed!")

#main

main()

#close connection

db.close()
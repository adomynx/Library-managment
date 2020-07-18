from Tkinter import *
import sqlite3
import datetime
import tkMessageBox

now = datetime.date.today()
print(str(now))
print(type(now))
base = Tk()
base.geometry("1280x700")
base.title("Library app")
base.configure(bg = "SlateBlue")
con = sqlite3.connect("library.db")
lb1 = Label(text = "Library Management System",font=("Times New Roman",30,"bold"),fg = 'white',bg = 'SlateBlue')
#lb1.grid(row = 0,column = 5)
#lb1.pack(pady = 10)
lb1.place(x=450, y = 0)

def IssueBook():
    a = Toplevel(base)
    a.geometry("500x500")
    a.title("Issue book")

    def search():
        cur = con.cursor()
        bn = str(tx2.get())
        bt = str(tx3.get())
        se = str(datetime.date.today())
        if bn != "":
            q = str("select title from book where book_no='" + bn + "'")
            cur.execute(q)
            data = cur.fetchone()
            if data == None:
                m = tkMessageBox.showinfo("Confirmation", "No such book available")
                if m=='ok':
                    a.destroy()
            else:
                tx3.delete(0, str(tx3.get()).__len__())
                tx3.insert(0, data[0])
                tx4.delete(0, str(tx4.get()).__len__())
                tx4.insert(0,se)

    def save():
        en = str(tx1.get())
        bn = str(tx2.get())
        bt = str(tx3.get())
        tx4.insert(0,str(datetime.date.today()))
        se = str(datetime.date.today())
        q = str("insert into issue_book(en_roll,b_no,b_title,iss_date,re_sat)values("
                +en+","+bn+",'"+bt+"','"+se+"','N')")
        con.execute(q)
        con.commit()
        m = tkMessageBox.showinfo("save","Data Saved Successfully")
        if m == 'ok':
            a.destroy()
    lb1 = Label(a,text = "Roll No",font=("Times New Roman",15,"italic"))
    lb1.pack()
    tx1 = Entry(a,width=15,font=("Times New Roman",15,"italic"))
    tx1.pack()
    tx1.focus()
    lb2 = Label(a,text = "Book No",font=("Times New Roman",15,"italic"))
    lb2.pack()
    tx2 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx2.pack()
    b2 = Button(a, text="Search", font=("Times New Roman", 15, "bold italic"), command=search)
    b2.pack()
    lb3 = Label(a,text = "Book Title",font=("Times New Roman",15,"italic"))
    lb3.pack()
    tx3 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx3.pack()
    lb4 = Label(a,text = "Issue Date",font=("Times New Roman",15,"italic"))
    lb4.pack()
    tx4 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx4.pack()
    b1 = Button(a,text = "Save",font=("Times New Roman",15,"bold italic"),command = save)
    b1.pack()
    a.mainloop()


def ReturnBook():
    a = Toplevel(base)
    a.geometry("500x500")
    a.title("Return book")

    def search():
        cur = con.cursor()
        bn = str(tx2.get())
        se = str(datetime.date.today())
        if bn != "":
            q = str("select title from book where book_no='" + bn + "'")
            cur.execute(q)
            data = cur.fetchone()
            if data == None:
                m = tkMessageBox.showinfo("Confirmation", "No such book available")
                if m == 'ok':
                    a.destroy()
            else:
                tx3.insert(0, data)
                tx4.insert(0, str(datetime.date.today()))
                tx5.insert(0, "Yes")
    def retn():
        cur = con.cursor()
        en = str(tx1.get())
        bn = str(tx2.get())
        se = str(datetime.date.today())
        q = str("select en_roll from issue_book where b_no='" + bn + "' and en_roll = '" + en + "'")
        cur.execute(q)
        data = cur.fetchone()
        if data == None:
            m = tkMessageBox.showinfo("Confirmation", "No such Record")
        else:
            e = data[0]
            print(e,en)

        if(en == e):
            s = "Y"
            q = str("update issue_book set re_date='" + se + "',re_sat='" + s
                    + "' where en_roll=" + en + " and b_no=" + bn)
            con.execute(q)
            con.commit()
            m = tkMessageBox.showinfo("save", "Data Saved Successfully")
            if m == 'ok':
                a.destroy()
        else:
            m = tkMessageBox.showinfo("Confirmation","Enter valid enroll no. or book no.")
            if m == 'ok':
                a.destroy()
    lb1 = Label(a, text="Enroll",font=("Times New Roman",15,"italic"))
    lb1.pack()
    tx1 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx1.pack()
    tx1.focus()
    lb2 = Label(a, text="Book No",font=("Times New Roman",15,"italic"))
    lb2.pack()
    tx2 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx2.pack()
    b2 = Button(a, text="Search", font=("Times New Roman", 15, "bold italic"), command=search)
    b2.pack()
    lb3 = Label(a, text="Book Title", font=("Times New Roman", 15, "italic"))
    lb3.pack()
    tx3 = Entry(a, width=15, font=("Times New Roman", 15, "italic"))
    tx3.pack()
    lb4 = Label(a, text="Return Date",font=("Times New Roman",15,"italic"))
    lb4.pack()
    tx4 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx4.pack()
    lb5 = Label(a, text="Return Status",font=("Times New Roman",15,"italic"))
    lb5.pack()
    tx5 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx5.pack()
    b1 = Button(a, text="Save", font=("Times New Roman", 15, "bold italic"), command=retn)
    b1.pack()

    a.mainloop()

def BookHistory():
    a = Toplevel(base)
    a.geometry("500x500")
    a.title("Book History")

    def save():
        m = tkMessageBox.showinfo("save", "Data Saved Successfully")
        if m == 'ok':
            a.destroy()

    lb1 = Label(a, text="Book no.",font=("Times New Roman",15,"italic"))
    lb1.pack()
    tx1 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx1.pack()
    tx1.focus()
    lb2 = Label(a, text="Book Title",font=("Times New Roman",15,"italic"))
    lb2.pack()
    tx2 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx2.pack()
    lb3 = Label(a, text="Book Author",font=("Times New Roman",15,"italic"))
    lb3.pack()
    tx3 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx3.pack()
    lb4 = Label(a, text="Book Publication",font=("Times New Roman",15,"italic"))
    lb4.pack()
    tx4 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx4.pack()
    lb5 = Label(a, text="Price",font=("Times New Roman",15,"italic"))
    lb5.pack()
    tx5 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx5.pack()
    lb6 = Label(a, text="Stock Entry Date",font=("Times New Roman",15,"italic"))
    lb6.pack()
    tx6 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx6.pack()

    b1 = Button(a, text="Save",font=("Times New Roman",15,"bold italic"), command=save)
    b1.pack()

    a.mainloop()

def StudentHistory():
    a = Toplevel(base)
    a.geometry("2000x600")
    a.title("Student Details")

    q = str("select * from issue_book")

    cur = con.cursor()
    cur.execute(q)
    ls = cur.fetchall()
    ls.insert(0,["Enroll no","Book no.","Book Title","Issue date","Return date","Return Status"])
    i = 0
    while (i < ls.__len__()):
        j = 0
        while (j < ls[i].__len__()):
            en = Entry(a, width=25,font=("Times New Roman",15,"italic"))
            en.grid(row=i, column=j)
            if(ls[i][j]==None):
                en.insert(0, "")
            else:
                en.insert(0, ls[i][j])
            en.configure(state='disabled')
            j = j + 1
        i = i + 1


def SearchBook():
    a = Toplevel(base)
    a.geometry("500x500")
    a.title("Search a Book")

    def search():
        cur = con.cursor()

        bn = str(tx1.get())
        bt = str(tx2.get())
        ba = str(tx3.get())
        bp = str(tx4.get())
        if bt!="" and ba=="" and bp=="":
            q = str("select book_no,author,publication from book where title='"+bt+"'")
            cur.execute(q)
            data = cur.fetchone()
            if data==None:
                m = tkMessageBox.showinfo("Confirmation","No such book available")
                if m == 'ok':
                    a.destroy()
            else:
                tx1.delete(0,str(tx1.get()).__len__())
                tx3.delete(0, str(tx3.get()).__len__())
                tx4.delete(0, str(tx4.get()).__len__())
                tx1.insert(0,data[0])
                tx3.insert(0, data[1])
                tx4.insert(0, data[2])

        if ba!="" and bt=="" and bp=="":
            q = str("select book_no,title,publication from book where author='"+ba+"'")
            cur.execute(q)
            data = cur.fetchone()
            if data==None:
                m = tkMessageBox.showinfo("Confirmation","No such book available")
                if m == 'ok':
                    a.destroy()
            else:
                tx1.delete(0,str(tx1.get()).__len__())
                tx2.delete(0, str(tx2.get()).__len__())
                tx4.delete(0, str(tx4.get()).__len__())
                tx1.insert(0,data[0])
                tx2.insert(0, data[1])
                tx4.insert(0, data[2])

    lb1 = Label(a, text="Book no.",font=("Times New Roman",15,"italic"))
    lb1.pack()
    tx1 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx1.pack()
    tx1.focus()
    lb2 = Label(a, text="Book Title",font=("Times New Roman",15,"italic"))
    lb2.pack()
    tx2 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx2.pack()

    lb3 = Label(a, text="Book Author",font=("Times New Roman",15,"italic"))
    lb3.pack()
    tx3 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx3.pack()

    lb4 = Label(a, text="Book Publication",font=("Times New Roman",15,"italic"))
    lb4.pack()
    tx4 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx4.pack()
    b1 = Button(a, text="Search",font=("Times New Roman",15,"bold italic"), command=search)
    b1.pack()

    a.mainloop()

def AddNewBook():
    a = Toplevel(base)
    a.geometry("500x500")
    a.title("Add New Book")

    def save():
        tx6.configure(text =str(datetime.date.today()) )
        bn = str(tx1.get())
        bt = str(tx2.get())
        ba = str(tx3.get())
        bp = str(tx4.get())
        pr = str(tx5.get())
        se = str(datetime.date.today())
        q = str("insert into book(book_no,title,author,publication,price,en_date)values("
                +bn+",'"+bt+"','"+ba+"','"+bp+"',"+pr+",'"+se+"')")
        con.execute(q)
        con.commit()
        m = tkMessageBox.showinfo("save", "Data Saved Successfully")
        if m == 'ok':
            a.destroy()

    lb1 = Label(a, text="Book no.",font=("Times New Roman",15,"italic"))
    lb1.pack()

    tx1 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx1.pack()
    tx1.focus()
    lb2 = Label(a, text="Book Title",font=("Times New Roman",15,"italic"))
    lb2.pack()
    tx2 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx2.pack()

    lb3 = Label(a, text="Book Author",font=("Times New Roman",15,"italic"))
    lb3.pack()
    tx3 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx3.pack()

    lb4 = Label(a, text="Book Publication",font=("Times New Roman",15,"italic"))
    lb4.pack()
    tx4 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx4.pack()
    lb5 = Label(a, text="Price",font=("Times New Roman",15,"italic"))
    lb5.pack()
    tx5 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx5.pack()
    lb6 = Label(a, text="Stock Entry Date",font=("Times New Roman",15,"italic"))
    lb6.pack()
    tx6 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx6.pack()

    b1 = Button(a, text="Save",font=("Times New Roman",15,"bold italic"), command=save)
    b1.pack()

    a.mainloop()

def NotReturnBook():
    a = Toplevel(base)
    a.geometry("500x500")
    a.title("Not Return Book")

    def search():
        cur = con.cursor()
        bn = str(tx2.get())
        se = str(datetime.date.today())

        if bn != "":
            q = str("select title from book where book_no='" + bn + "'")
            cur.execute(q)
            data = cur.fetchone()
            if data == None:
                m = tkMessageBox.showinfo("Confirmation", "No such book available")
                if m == 'ok':
                    a.destroy()
            else:
                tx3.insert(0, data)

    def get():
        en = str(tx1.get())
        cur = con.cursor()
        bn = str(tx2.get())

        qu = str("select en_roll from issue_book where b_no='" + bn + "'")
        cur.execute(qu)
        data = cur.fetchone()
        if data == None:
            m = tkMessageBox.showinfo("Confirmation", "No such book Present")
            if m == 'ok':
                a.destroy()
        else:
            e = data[0]

        if (en == e):
            if bn != "":
                q = str("select iss_date,re_date,re_sat from issue_book where b_no='" + bn + "'")
                cur.execute(q)
                data = cur.fetchone()
                if data == None:
                    m = tkMessageBox.showinfo("Confirmation", "No such book available")
                    if m == 'ok':
                        a.destroy()
                else:
                    if (data[1] == None):
                        tx4.insert(0, data[0])
                        tx5.insert(0, "NULL")
                    else:
                        tx4.insert(0, data[0])
                        tx5.insert(0, data[1])
                        tx6.insert(0, data[2])
        else:
            m = tkMessageBox.showinfo("Confirmation", "Enter valid enroll no. or book no.")
            if m == 'ok':
                a.destroy()


    lb1 = Label(a, text="Enroll",font=("Times New Roman",15,"italic"))
    lb1.pack()
    tx1 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx1.pack()
    tx1.focus()
    lb2 = Label(a, text="Book No",font=("Times New Roman",15,"italic"))
    lb2.pack()
    tx2 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx2.pack()
    b2 = Button(a, text="Search", font=("Times New Roman", 15, "bold italic"), command=search)
    b2.pack()
    lb3 = Label(a, text="Book Title",font=("Times New Roman",15,"italic"))
    lb3.pack()
    tx3 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx3.pack()
    b3 = Button(a, text="Get Details", font=("Times New Roman", 15, "bold italic"), command=get)
    b3.pack()
    lb4 = Label(a, text="Issue Date",font=("Times New Roman",15,"italic"))
    lb4.pack()
    tx4 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx4.pack()
    lb5 = Label(a, text="Return Date",font=("Times New Roman",15,"italic"))
    lb5.pack()
    tx5 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx5.pack()
    lb6 = Label(a, text="Return Status",font=("Times New Roman",15,"italic"))
    lb6.pack()
    tx6 = Entry(a, width=15,font=("Times New Roman",15,"italic"))
    tx6.pack()

    # b1 = Button(a, text="Save",font=("Times New Roman",15,"bold italic"), command=save)
    # b1.pack()

    a.mainloop()

def close():
    de = tkMessageBox.askyesno("Confirmation","Do you want to close this Application?")
    if de==1:
        base.destroy()


b1 = Button(base,text="Issue book",width = 13,height = 3,
            font=("Times New Roman",15,"bold italic"),command = IssueBook)
#b1.grid(row = 3,column = 1)
b1.place(x = 20,y = 100)

b2 = Button(base,text="Return book",width = 13,height = 3,
            font=("Times New Roman",15,"bold italic"),command = ReturnBook)
#b2.grid(row = 3,column = 2)
b2.place(x = 200,y = 100)

b3 = Button(base,text="Book History",width = 13,height = 3,
            font=("Times New Roman",15,"bold italic"),command = BookHistory)
#b3.grid(row = 3,column = 3)
b3.place(x = 380,y = 100)

b4 = Button(base,text="Student History",width = 13,height = 3,
            font=("Times New Roman",15,"bold italic"),command = StudentHistory)
#b4.grid(row = 3,column = 4)
b4.place(x = 560,y = 100)



b6 = Button(base,text="Add new book",width = 13,height = 3,
            font=("Times New Roman",15,"bold italic"),command = AddNewBook)
#b6.grid(row = 3,column = 6)
b6.place(x = 920,y = 100)



bu = Button(base,text="Close",width = 10,height = 3,
            font=("Times New Roman",18,"bold"),bg = "Red",fg = "White",command = close)
#bu.grid(row = 5,column = 5)
bu.place(x=1100,y = 500)
base.mainloop()
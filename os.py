from tkinter import *
from turtle import *
from tkinter import PhotoImage
import webbrowser
from translate import Translator
import wikipedia
import os
def db():
    import sqlite3
    
    class Database:
        def __init__(self, db):
            self.con = sqlite3.connect(db)
            self.cur = self.con.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS employees(
                id Integer Primary Key,
                name text,
                age text,
                doj text,
                email text,
                gender text,
                contact text,
                address text
            )
            """
            self.cur.execute(sql)
            self.con.commit()
    
        # Insert Function
        def insert(self, name, age, doj, email, gender, contact, address):
            self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                             (name, age, doj, email, gender, contact, address))
            self.con.commit()
    
        # Fetch All Data from DB
        def fetch(self):
            self.cur.execute("SELECT * from employees")
            rows = self.cur.fetchall()
            # print(rows)
            return rows
    
        # Delete a Record in DB
        def remove(self, id):
            self.cur.execute("delete from employees where id=?", (id,))
            self.con.commit()
    
        # Update a Record in DB
        def update(self, id, name, age, doj, email, gender, contact, address):
            self.cur.execute(
                "update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                (name, age, doj, email, gender, contact, address, id))
            self.con.commit()
    
    
    
    
    from tkinter import ttk
    from tkinter import messagebox
    
    
    db = Database("Employee.db")
    root = Tk()
    root.title("Employee Management System for DURKATHON")
    root.geometry("1920x1080+0+0")
    root.config(bg="#2c3e50")
    root.state("zoomed")
    btn=Button(root,text="kill",command=root.destroy)
    btn.config(font=("callibri",24,"bold"),fg="black",bg="red")
    btn.pack(side=RIGHT)
    
    name = StringVar()
    age = StringVar()
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()
    
    # Entries Frame
    entries_frame = Frame(root, bg="#535c68")
    entries_frame.pack(side=TOP, fill=X)
    title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
    title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
    
    lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")
    
    lbldoj = Label(entries_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white")
    lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
    txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    
    lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")
    
    lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")
    
    lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")
    
    lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    
    txtAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
    txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")
    
    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        #print(row)
        name.set(row[1])
        age.set(row[2])
        doj.set(row[3])
        email.set(row[4])
        gender.set(row[5])
        contact.set(row[6])
        txtAddress.delete(1.0, END)
        txtAddress.insert(END, row[7])
    
    def dispalyAll():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)
    
    
    def add_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
                1.0, END) == "":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(
                1.0, END))
        messagebox.showinfo("Success", "Record Inserted")
        clearAll()
        dispalyAll()
    
    
    
    def update_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
                1.0, END) == "":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
                  txtAddress.get(
                      1.0, END))
        messagebox.showinfo("Success", "Record Update")
        clearAll()
        dispalyAll()
    
    
    def delete_employee():
        db.remove(row[0])
        clearAll()
        dispalyAll()
    
    
    def clearAll():
        name.set("")
        age.set("")
        doj.set("")
        gender.set("")
        email.set("")
        contact.set("")
        txtAddress.delete(1.0, END)
    
    
    btn_frame = Frame(entries_frame, bg="#535c68")
    btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)
    
    # Table Frame
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),
                    rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="ID")
    tv.column("1", width=5)
    tv.heading("2", text="Name")
    tv.heading("3", text="Age")
    tv.column("3", width=5)
    tv.heading("4", text="D.O.B")
    tv.column("4", width=10)
    tv.heading("5", text="Email")
    tv.heading("6", text="Gender")
    tv.column("6", width=10)
    tv.heading("7", text="Contact")
    tv.heading("8", text="Address")
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getData)
    tv.pack(fill=X)
    
    dispalyAll()
    root.mainloop()
from tkinter import PhotoImage

root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="white")
root.title("DURKESH KUMAR PERAK OS DISTRIBUTION")
msg=Label(root,text="DURKESH KUMAR PERAK OS DISTRIBUTION")
msg.config(font=("callibri",24,"bold"))
#msg.grid(row=0,column=0,columnspan=2)
msg.pack(side=TOP)
btn=Button(root,text="kill",command=root.destroy)
btn.config(bg="red",fg="black",font=("callibri",16,"bold"))
#btn.grid(row=0,column=1,padx=50,pady=50)
btn.pack(side=TOP,padx=300,pady=10)
def sam():
    import webbrowser
    webbrowser.open("https://win11.blueedge.me/")

t=Button(root,text="WINDOWS 11",command=sam)
t.config(bg="#ADD8E6",fg="black",font=("callibri",16,"bold"))

t.pack(side=TOP,padx=20)

k=Button(root,text="DATABASE",command=db)
k.config(bg="#ADD8E6",fg="black",font=("callibri",16,"bold"))
k.pack(side=LEFT)
def tur():
    bgcolor("black")
    pencolor("green")
    pensize(1)
    speed(0)
    b=0
    while b<200:
        right(b)
        forward(b*3)
        b+=1
z=Button(root,text="BOOT UP",command=tur)
z.config(bg="#ADD8E6",fg="black",font=("callibri",16,"bold"))
z.pack(side=RIGHT)


img=PhotoImage(file="thumb-1-1024x683.png")
lbl=Label(root,image=img)
lbl.config(width=7000, height=400)
lbl.pack()
def search():
    import webbrowser
    webbrowser.open("https://www.google.com")
s=Button(root,text="GOOGLE",command=search)
s.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
s.pack(side=LEFT,padx=10,pady=10)
def tam():
    import webbrowser
    webbrowser.open("https://github.com/")
t=Button(root,text="GIT HUB",command=tam)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)
def sample():
    import webbrowser
    webbrowser.open("https://www.linkedin.com")

t=Button(root,text="LINKED IN",command=sample)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)
def simple():
    import webbrowser
    webbrowser.open("https://www.whatsapp.com")

t=Button(root,text="WHATSAPP",command=simple)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)


def net():
    import webbrowser
    webbrowser.open("https://www.twitter.com")

t=Button(root,text="TWITTER",command=net)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)

def display():

    img=PhotoImage(file="thumb-1-1024x683.png")
    
    
    lbl=Label(root,image=img)
    lbl.config(width=7000, height=400)
    lbl.pack()
def new():
    root=Tk()
    root.attributes("-fullscreen",True)
    root.config(bg="white")
    root.title("OTHERS")
    
    msg=Label(root,text="DURKESH KUMAR ENTERTIMENTS")
    msg.config(font=("callibri",24,"bold"))
    msg.pack()
    btn=Button(root,text="kill",command=root.destroy)
    btn.config(font=("callibri",16,"bold"),fg="black",bg="red")
    btn.pack(padx=20,pady=20)
    display()
    

    def you():
        webbrowser.open_new_tab("https://www.youtube.com")
    x=Button(root,text="YOUTUBE",command=you)
    x.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    x.pack(side=LEFT,padx=20,pady=20)
    def insta():
        webbrowser.open_new_tab("https://www.instagram.com")
    
    y=Button(root,text="INSTAGRAM",command=insta)
    y.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    y.pack(side=LEFT,padx=20,pady=20)
    
    def face():
        webbrowser.open_new_tab("https://www.facebook.com")
    
    y=Button(root,text="FACEBOOK",command=face)
    y.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    y.pack(side=LEFT,padx=20,pady=20)
    def tel():
        webbrowser.open_new_tab("https://www.telegram.com")
    
    y=Button(root,text="TELEGRAM",command=tel)
    y.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    y.pack(side=LEFT,padx=20,pady=20)
    def translator():
        root=Tk()
        root.attributes("-fullscreen",True)
        # root.config(bg="white")
        root.title("OTHERS")
        
        msg=Label(root,text="DURKESH KUMAR TRANSLATOR")
        msg.config(font=("callibri",24,"bold"))
        msg.pack()
        btn=Button(root,text="kill",command=root.destroy)
        btn.config(font=("callibri",16,"bold"),fg="black",bg="red")
        btn.pack(padx=20,pady=20)
        lbl=Label(root,text="INPUT LANGUAGE :")
        lbl.config(font=("callibri",16,"bold"))
        lbl.pack()
    
        entry=Entry(root)
        entry.config(width=50,font=("callibri",16,"bold"))
        entry.pack()
    
        lbl=Label(root,text="OUTPUT LANGUAGE :")
        lbl.config(font=("callibri",16,"bold"))
        lbl.pack()
    
        end=Entry(root)
        end.config(width=50,font=("callibri",16,"bold"))
        end.pack()
    
        lbl=Label(root,text="INFORMATION :")
        lbl.config(font=("callibri",16,"bold"))
        lbl.pack()
    
        info=Entry(root)
        info.config(width=50,font=("callibri",16,"bold"))
        info.pack()
        def trans():
            a=entry.get()
            b=end.get()
            c=info.get()
            y=Translator(from_lang=a,to_lang=b)
            x=y.translate(c)
            lbl=Label(root,text=x)
            lbl.config(font=("callibri",16,"bold"))
            lbl.pack()
    
    
        btn=Button(root,text="TRANSLATE",command=trans)
        btn.config(font=("callibri",16,"bold"),fg="black",bg="green")
        btn.pack(padx=20,pady=20)
    btn=Button(root,text="TRANSLATOR",command=translator)
    btn.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    btn.pack(side=LEFT,padx=20,pady=20)
    
    def search():
        root=Tk()
        root.title("SEARCH ENGINE")
        root.attributes("-fullscreen",True)
        msg=Label(root,text="DURKESH KUMAR TRANSLATOR")
        msg.config(font=("callibri",24,"bold"))
        msg.pack()
        btn=Button(root,text="kill",command=root.destroy)
        btn.config(font=("callibri",16,"bold"),fg="black",bg="red")
        btn.pack(padx=20,pady=20)
        lbl=Label(root,text="ENTER A DATA TO SEARCH :")
        lbl.config(font=("callibri",16,"bold"))
        lbl.pack(padx=20,pady=20)
    
        entry=Entry(root)
        entry.config(width=50,font=("callibri",16,"bold"))
        entry.pack(padx=20,pady=20)
        def search():
            x=entry.get()
            y=wikipedia.summary(x,sentences=1)
            lbl=Label(root,text=y)
            lbl.config(font=("callibri",16,"bold"),fg="black",bg="yellow",width=100)
            lbl.pack()
        btn=Button(root,text="search",command=search)
        btn.config(font=("callibir",16,"bold"),fg="black",bg="green")
        btn.pack()
        
    
    
    btn=Button(root,text="SEARCH ENGINE",command=search)
    btn.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    btn.pack(side=LEFT,padx=20,pady=20)
    def shut():
        os.system("shutdown /s /t 1")
    btn=Button(root,text="SHUTDOWN",command=shut)
    btn.config(font=("callibri",16,"bold"),fg="black",bg="pink")
    btn.pack(side=LEFT,padx=20,pady=20)
    root.mainloop()
    
#others
t=Button(root,text="OTHERS",command=new)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=40)
t.pack(side=LEFT,padx=10,pady=10)


root.mainloop()

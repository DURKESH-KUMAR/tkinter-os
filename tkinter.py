from tkinter import *
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
btn.pack(side=TOP,padx=180,pady=10)
def sam():
    import webbrowser
    webbrowser.open("https://win11.blueedge.me/")

t=Button(root,text="WINDOWS 11",command=sam)
t.config(bg="#ADD8E6",fg="black",font=("callibri",16,"bold"),padx=20,pady=20)
t.pack(side=TOP,padx=20,pady=20)
img=PhotoImage(file="thumb-1-1024x683.png")
lbl=Label(root,image=img)
lbl.config(width=600, height=400)
lbl.pack()
def search():
    import webbrowser
    webbrowser.open("https://www.google.com")
s=Button(root,text="SEARCH ENGINE",command=search)
s.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
s.pack(side=LEFT,padx=10,pady=10)
def tam():
    import webbrowser
    webbrowser.open("https://www.instagram.com")

    

    
t=Button(root,text="INSTAGRAM",command=tam)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)
def sample():
    import webbrowser
    webbrowser.open("https://www.facebook.com")

t=Button(root,text="FACEBOOK",command=sample)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)
def simple():
    import webbrowser
    webbrowser.open("https://www.whatsapp.com")

t=Button(root,text="WHATSAPP",command=simple)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)
def new():
    import webbrowser
    webbrowser.open("https://www.youtube.com")

t=Button(root,text="YOUTUBE",command=new)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=40)
t.pack(side=LEFT,padx=10,pady=10)
def net():
    import webbrowser
    webbrowser.open("https://www.twitter.com")

t=Button(root,text="TWITTER",command=net)
t.config(bg="pink",fg="black",font=("callibri",16,"bold"),padx=20)
t.pack(side=LEFT,padx=10,pady=10)
root.mainloop()

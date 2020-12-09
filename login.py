import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox

interface=Tk()
interface.title("LOGIN")
interface.geometry("500x500")
email=StringVar()
password=StringVar()

def register():
    interface.destroy()
    os.system('new_user.py')
    

def admin():
    interface.destroy()
    os.system('admin.py')
    
    
def submit():
    j=0
    try:
        conn=sqlite3.connect('database.db')
        print("CONNECTED")
    except:
        print("NOT CONNECTED")
    m=conn.execute("select Mail_Address,Password from data")
    mail=email.get()
    key=password.get()
    if(len(mail)==0 or len(key)==0):
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")
        obj.func_1()
    if ('@' not in mail):
        messagebox.showinfo("!!ERROR!!", "PLEASE PROVIDE A VALID MAIL ID")
        obj.func_1()
    else:
        pass
    if(len(key)<6):
        messagebox.showinfo("!!ERROR!!","PLEASE ENSURE LENGTH OF PASSWORD(ATLEAST 6)")
        obj.func_1()
    else:
        pass
    for i in m:
        if(mail in i[0]):
            if(key in i[1]):
                conn.commit()
                
                os.system('booking.py')
            else:
                messagebox.showinfo("!!ERROR!!","PASSWORD IS INCORRECT")
        else:
            pass
Label(interface,text="EMAIL: ",font='cambria').place(x=10,y=100)
Entry(interface,textvar=email,font='cambria',bd=2).place(x=120,y=100)
Label(interface,text="PASSWORD: ",font='cambria').place(x=10,y=150)
Entry(interface,textvar=password,font='cambria',bd=2,show="*").place(x=120,y=150)
class A:
    def func_1(self):
        Button(interface,text="LOGIN",command=submit).place(x=190,y=210)
        
        
Button(interface,text="REGISTER",command=register).place(x=250,y=210)
Button(interface,text="ADMIN",command=admin).place(x=120,y=210)  
obj=A()
obj.func_1()
interface.mainloop()

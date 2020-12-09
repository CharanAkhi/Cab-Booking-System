import tkinter
from tkinter import*
import sqlite3
import os

interface=Tk()
interface.title('LPU CAB BOOKING SYSTEM')
interface.geometry("500x500")

#function 1
def login():
    interface.destroy()
    os.system("login.py")

#function 2
def new_user():
    interface.destroy()
    os.system('new_user.py')

#function 3
def available_routes():
    interface.destroy()
    os.system('available_routes.py')

#buttons in interface

Button(interface,text="LOGIN",command=login,bg="red", fg="white").place(x=230,y=200)
Button(interface,text="NEW USER",command=new_user,bg="red", fg="white").place(x=220,y=240)
Button(interface,text="AVAILABLE ROUTES",command=available_routes,bg="red", fg="white").place(x=200,y=280)

interface.mainloop()

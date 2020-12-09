import tkinter
from tkinter import*
import sqlite3
import os

interface1=Tk()
interface1.title("SESSION")
interface1.geometry("350x350")
conn4=sqlite3.connect('transaction.db')
def done():
    interface1.destroy()
a=conn4.execute('select Session_Id from data')
c=0
for i in a:
    
    z=i[c]
    
Label(interface1,text="Please Note Down",font='cambria',bd=2).place(x=100,y=10)
Label(interface1,text="SESSION_ID : ",font='cambria',bd=2).place(x=10,y=60)
Label(interface1,text=z,font='cambria',bd=2).place(x=150,y=60)
Button(interface1, text="DONE", command=done).place(x=120,y=120)
conn4.commit()
interface1.mainloop()

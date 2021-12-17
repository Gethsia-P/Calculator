# -*- coding: utf-8 -*-
from tkinter import *


window=Tk()
window.title("Calculator") 
window.geometry("350x350")
entry=Entry(window,width=40,borderwidth=5)
entry.place(x=5,y=5)

def click(n):
    c=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(c)+str(n))
button=Button(window,text="1",width=10,command=lambda:click(1),bg="blue")
button.place(x=20,y=60)
button=Button(window,text="2",width=10,command=lambda:click(2),bg="blue")
button.place(x=100,y=60)
button=Button(window,text="3",width=10,command=lambda:click(3),bg="blue")
button.place(x=180,y=60)
button=Button(window,text="4",width=10,command=lambda:click(4),bg="blue")
button.place(x=20,y=100)
button=Button(window,text="5",width=10,command=lambda:click(5),bg="blue")
button.place(x=100,y=100)
button=Button(window,text="6",width=10,command=lambda:click(6),bg="blue")
button.place(x=180,y=100)
button=Button(window,text="7",width=10,command=lambda:click(7),bg="blue")
button.place(x=20,y=140)
button=Button(window,text="8",width=10,command=lambda:click(8),bg="blue")
button.place(x=100,y=140)
button=Button(window,text="9",width=10,command=lambda:click(9),bg="blue")
button.place(x=180,y=140)
button=Button(window,text="0",width=10,command=lambda:click(0),bg="blue")
button.place(x=20,y=180)

def div():
    n1=entry.get()
    global a
    global math
    math='division'
    a=int(n1)
    entry.delete(0,END)
button=Button(window,text="/",width=10,command=div,bg="blue")
button.place(x=100,y=180)

def mul():
    n1=entry.get()
    global a
    global math
    math='multiplication'
    a=int(n1)
    entry.delete(0,END)
button=Button(window,text="*",width=10,command=mul,bg="blue")
button.place(x=180,y=180)

def add():
    n1=entry.get()
    global a
    global math
    math='addition'
    a=int(n1)
    entry.delete(0,END)
button=Button(window,text="+",width=10,command=add,bg="blue")
button.place(x=20,y=220)

def sub():
    n1=entry.get()
    global a
    global math
    math='subtraction'
    a=int(n1)
    entry.delete(0,END)
button=Button(window,text="-",width=10,command=sub,bg="blue")
button.place(x=100,y=220)

def equal():
    n2=entry.get()
    entry.delete(0,END)
    if math=='addition':
        entry.insert(0,a+int(n2))
        
    elif math=='subtraction':
        entry.insert(0,a-int(n2))
        
    elif math=='division':
        entry.insert(0,a/int(n2))
        
    elif math=='multiplication':
        entry.insert(0,a*int(n2))
        
    
button=Button(window,text="=",width=10,height=5,command=equal,bg="blue")
button.place(x=265,y=60)
def clear():
    entry.delete(0,END)
button=Button(window,text="CLR",width=10,height=5,command=clear,bg="blue")
button.place(x=265,y=160)

window.mainloop()
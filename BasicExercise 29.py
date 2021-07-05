#!/usr/bin/env python2.6
#_*_coding:utf8_*_


from Tkinter import *
v0=Tk()

imagen1=PhotoImage(file="/home/rpetit/Python/estr.png")
label1 = Label(v0, image=imagen1)
label1.grid(row=1,column=1)
v0.mainloop()

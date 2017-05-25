# This is Project work for the Garphical scientific calculator
# by Himanshu Vishwakarma
# cal.py

from tkinter import *
#from main import *

def allclear(entry):
    entry.delete(0,END)

def action(entry, argi):
    entry.insert(END,argi)

def equals(entry):
    exp = entry.get()
    try:
        entry.value = eval(exp)# evaluate the expression using the eval function
    except SyntaxError or NameError:
        entry.delete(0,END)
        entry.insert(0,'Invalid Input!')
    else:
        entry.delete(0,END)
        entry.insert(0,entry.value)

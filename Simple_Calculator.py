#main function for the simple calculator GUI
from tkinter import *

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

def main():

    root = Tk()
    root.title('Calculator')
    root.resizable(width=False, height=False)

    inputext = StringVar()#entry text variable

    topframe = Frame(root,bg='white').grid()#entry frame variable
    entry = Entry(topframe, textvariable = inputext, bd=10, insertwidth = 1,font = 'Helvetica 20', width = 16, justify = RIGHT)
    entry.grid()
    root.bind('<Return>', lambda x: equals(entry))

    buttonframe = Frame(root)
    buttonframe.grid()
    Button(buttonframe,text='(', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '(')).grid(row = 0, column = 3)
    Button(buttonframe,text=')', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, ')')).grid(row = 0, column = 4)
    Button(buttonframe,text='%', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '%')).grid(row = 0, column = 5)
    Button(buttonframe,text='AC', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: allclear(entry)).grid(row = 0, column = 6)
    Button(buttonframe,text='7', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 7)).grid(row = 1, column = 3)
    Button(buttonframe,text='8', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 8)).grid(row = 1, column = 4)
    Button(buttonframe,text='9', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 9)).grid(row = 1, column = 5)
    Button(buttonframe,text='/', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '/')).grid(row = 1, column = 6)
    Button(buttonframe,text='4', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 4)).grid(row = 2, column = 3)
    Button(buttonframe,text='5', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 5)).grid(row = 2, column = 4)
    Button(buttonframe,text='6', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 6)).grid(row = 2, column = 5)
    Button(buttonframe,text='x', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '*')).grid(row = 2, column = 6)
    Button(buttonframe,text='1', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 1)).grid(row = 3, column = 3)
    Button(buttonframe,text='2', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 2)).grid(row = 3, column = 4)
    Button(buttonframe,text='3', padx = 16, bd = 8, fg = 'black', bg='white', height = 1, width = 2, command = lambda: action(entry, 3)).grid(row = 3, column = 5)
    Button(buttonframe,text='-', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '-')).grid(row = 3, column = 6)
    Button(buttonframe,text='0', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, 0)).grid(row = 4, column = 3)
    Button(buttonframe,text='.', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '.')).grid(row = 4, column = 4)
    Button(buttonframe,text='+', padx = 16, bd = 8, fg = 'black', height = 1, width = 2, command = lambda: action(entry, '+')).grid(row = 4, column = 5)
    Button(buttonframe,text='=', padx = 16, bd = 8, fg = 'black', bg='lightblue', height = 1, width = 2, command = lambda: equals(entry)).grid(row = 4, column = 6)

    root.mainloop()


if __name__ == "__main__" : main()

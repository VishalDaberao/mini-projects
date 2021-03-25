from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os.path
root = Tk()
root.wm_iconbitmap('clogo.ico')
root.configure(background="#f2f2f2")
root.title("Code Saver")
root.geometry('602x539')
root.resizable(False,False)
def click1():
    
    nam = fname.get()
    we = "'"
    we1 = '"'
    err=2
    for i in nam:
        if i == "'" or i == '"':
            err = 1
    if err == 1:
        messagebox.showwarning(title="error", message="Name can not contain "+we+" or "+we1)
        fname.delete(0,'end')
        code.delete('1.0','end-1c')
    elif err != 1:
        chk = os.path.exists('E:/Data/Text/'+nam+'.txt')
        if chk == True:
            messagebox.showwarning(title='error', message='File name '+nam+'.txt already exists')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')
        elif chk == False:
            f = open('E:/Data/Text/'+nam+'.txt','wt')
            f.write(code.get('1.0','end-1c'))
            messagebox.showinfo(title='Saved', message='Saved successfully')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')

def click2():
    
    nam = fname.get()
    we = "'"
    we1 = '"'
    err=2
    for i in nam:
        if i == "'" or i == '"':
            err = 1
    if err == 1:
        messagebox.showwarning(title="error", message="Name can not contain "+we+" or "+we1)
        fname.delete(0,'end')
        code.delete('1.0','end-1c')
    elif err != 1:
        chk = os.path.exists('E:/Data/Python/'+nam+'.py')
        if chk == True:
            messagebox.showwarning(title='error', message='File name '+nam+'.py already exists')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')
        elif chk == False:
            f = open('E:/Data/Python/'+nam+'.py','wt')
            f.write(code.get('1.0','end-1c'))
            messagebox.showinfo(title='Saved', message='Saved successfully')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')

def click3():
    
    nam = fname.get()
    we = "'"
    we1 = '"'
    err=2
    for i in nam:
        if i == "'" or i == '"':
            err = 1
    if err == 1:
        messagebox.showwarning(title="error", message="Name can not contain "+we+" or "+we1)
        fname.delete(0,'end')
        code.delete('1.0','end-1c')
    elif err != 1:
        chk = os.path.exists('E:/Data/c/'+nam+'.c')
        if chk == True:
            messagebox.showwarning(title='error', message='File name '+nam+'.c already exists')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')
        elif chk == False:
            f = open('E:/Data/c/'+nam+'.c','wt')
            f.write(code.get('1.0','end-1c'))
            messagebox.showinfo(title='Saved', message='Saved successfully')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')

def click4():
    
    nam = fname.get()
    we = "'"
    we1 = '"'
    err=2
    for i in nam:
        if i == "'" or i == '"':
            err = 1
    if err == 1:
        messagebox.showwarning(title="error", message="Name can not contain "+we+" or "+we1)
        fname.delete(0,'end')
        code.delete('1.0','end-1c')
    elif err != 1:
        chk = os.path.exists('E:/Data/cpp/'+nam+'.cpp')
        if chk == True:
            messagebox.showwarning(title='error', message='File name '+nam+'.cpp already exists')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')
        elif chk == False:
            f = open('E:/Data/cpp/'+nam+'.cpp','wt')
            f.write(code.get('1.0','end-1c'))
            messagebox.showinfo(title='Saved', message='Saved successfully')
            fname.delete(0,'end')
            code.delete('1.0','end-1c')
    


#text input field
flabel = Label(root, text="File Name:", font=("Verdana",12))
flabel.place(x=0,y=0)
fname = Entry(root, width=30, font=("Verdana",12))
fname.pack()
clabel = Label(root, text="Code:", font=("Verdana",12))
clabel.pack(pady=10)
code = Text(root, width=70, height=25)
code.pack()
#button field
txt = Button(root, text='TXT', command=click1)
txt.pack(padx=10, side=LEFT)
py = Button(root, text="Python", command=click2)
py.pack(padx=10,side=LEFT)
c = Button(root, text="C",command=click3)
c.pack(padx=10,side=LEFT)
cpp = Button(root, text="C++", command=click4)
cpp.pack(padx=10, side=LEFT)
#labels

root.mainloop()

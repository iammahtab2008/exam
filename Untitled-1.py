from tkinter import *
from tkinter import messagebox
import database1

win = Tk()
win.title('Login Form')
win.geometry('380x280+400+100')
win.configure(bg='#ffeee6')

db = database1.Database('e:/project3/database.db')

#=======func===========
def sign_up():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    if email == '' or password == '':
        messagebox.showerror('Error', 'Email and Password are required!')
        return
    else:
        db.insert(fname, lname, email, password)
        messagebox.showinfo('Success', 'User added successfully!')
        clear()

def sign_in():
    email = ent_email.get()
    password = ent_password.get()
    if email == '' or password == '':
        messagebox.showerror('Error', 'Email and Password are required!')
        return
    else:
        data = db.find_user(email, password)
        if data:
            messagebox.showinfo('Welcome', f'{data[0]} {data[1]}, welcome!')
            clear()
        else:
            messagebox.showerror('Error', 'Invalid email or password.')
        

def clear():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_email.delete(0, END)
    ent_password.delete(0, END)
    ent_fname.focus_set()

#=======widget===========
'''label'''
lbl_fname = Label(win, text='Fname', font='cambria 16 bold', bg='#ffeee6')
lbl_fname.grid(row=0, column=0, padx=10, pady=10)

lbl_lname = Label(win, text='Lname', font='cambria 16 bold', bg='#ffeee6')
lbl_lname.grid(row=1, column=0, padx=10, pady=10)

lbl_email = Label(win, text='Email', font='cambria 16 bold', bg='#ffeee6')
lbl_email.grid(row=2, column=0, padx=10, pady=10)

lbl_password = Label(win, text='Password', font='cambria 16 bold', bg='#ffeee6')
lbl_password.grid(row=3, column=0, padx=25, pady=10)

lbl_star1 = Label(win, text='*', font='cambria 16 bold', bg='#ffeee6', fg='red')
lbl_star1.place(x=8, y=115)

lbl_star2 = Label(win, text='*', font='cambria 16 bold', bg='#ffeee6', fg='red')
lbl_star2.place(x=8, y=170)

'''entry'''
ent_fname = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_fname.grid(row=0, column=1, padx=2, pady=10)

ent_lname = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_lname.grid(row=1, column=1, padx=2, pady=10)

ent_email = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_email.grid(row=2, column=1, padx=2, pady=10)

ent_password = Entry(win, font='cambria 14 bold', bg='#ffccff', width=16)
ent_password.grid(row=3, column=1, padx=2, pady=10)

'''button'''
btn_sign_up = Button(win, text='sign up', font='cambria 14 bold', bg='#ffccff', width=11, command=sign_up)
btn_sign_up.grid(row=4, column=0, padx=20, pady=10)

btn_sign_in = Button(win, text='sign in', font='cambria 14 bold', bg='#ffccff', width=11, command=sign_in)
btn_sign_in.grid(row=4, column=1, padx=0, pady=10)

win.mainloop()

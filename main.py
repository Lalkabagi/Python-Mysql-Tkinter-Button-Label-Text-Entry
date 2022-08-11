import pymysql
import tkinter as tk
from tkinter import messagebox
from tkinter import *

w = tk.Tk()

def button():
    if e1.get() != '' and e2.get() != '' and e3.get() != '':
        cursor.execute('INSERT INTO users (name, pasword, email) VALUES ("{}", "{}", "{}")'.format(e1.get(), e2.get(), e3.get()))
        connection.commit()
    else:
        messagebox.showerror('Error','The line is empty.')
connection = pymysql.connect(
                                host='localhost',
                                database='tksql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

f = tk.Frame(master = w,width = 200,height = 100,bg ="green")
f.pack(fill = tk.BOTH,side = tk.TOP,expand = True)
f2 =tk.Frame(master = w,width = 200,height = 100,bg = "yellow")
f2.pack(fill = tk.BOTH,side = tk.BOTTOM,expand = True)

e1 = tk.Entry(master = f,width = 25)
e2 = tk.Entry(master = f,width = 25)
e3 = tk.Entry(master = f,width = 25)
e1.grid(row = 0,column = 0,padx =10,pady =10)
e2.grid(row = 0,column = 1,padx =10,pady =10)
e3.grid(row = 0,column = 2,padx =10,pady =10)

b =tk.Button(master = f2,text = "Зберегти",width = 35,height = 5,command = button)
b.pack()

w.mainloop()

cursor.close()
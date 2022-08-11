import pymysql
import tkinter as tk
from tkinter import messagebox
from tkinter import *

w = tk.Tk()

def button():
    if e.get() !='':
        id = int(e.get())
        cursor.execute("SELECT name, pasword, email FROM users where id = {}".format(id))
        info = cursor.fetchall()
        l2.config(text="{}".format(info))
    else:    
        messagebox.showerror('Erorr','Line is empty')
        
connection = pymysql.connect(
                                host='localhost',
                                database='tksql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()  
f = tk.Frame(master = w,width = 100,height = 200,bg ="green")                              
f.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
f2 = tk.Frame(master = w,width = 100,height = 200, bg = "violet")
f2.pack(fill = tk.BOTH, expand = True)
f3 = tk.Frame(master = w,width = 100,height = 200, bg = "pink")
f3.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)

e = tk.Entry(master = f,width = 25)
e.grid(row =0,column =2,padx =10,pady =10)
l = tk.Label(master = f,text = "Please enter id:",bg ="green",fg = "white")
l.grid(row =0,column =1,padx =10,pady =10)
b = tk.Button(master = f2,text = "Вивести результат: ",command = button)
b.pack()
l2 = tk.Label(master = f3,text = "",bg ="pink")
l2.pack() 
w.mainloop()

cursor.close
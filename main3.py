import pymysql
import tkinter as tk
from tkinter import messagebox
from tkinter import *

w = tk.Tk()

def button():
    cursor.execute('SELECT name, pasword ,email FROM users')
    info = cursor.fetchall()
    t.insert(tk.END,"{}".format(info))
connection = pymysql.connect(
                                host='localhost',
                                database='tksql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()  
f = tk.Frame(master = w,width = 100,height = 200,bg ="green")                              
f.pack(fill = tk.BOTH, side = tk.TOP, expand = True)
f2 = tk.Frame(master = w,width = 100,height = 200,bg ="blue")                              
f2.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)

t = tk.Text(master = f,width = 19,height =10)
t.pack()
b = tk.Button(master = f2,text = "Вивести",command = button)
b.pack()
w.mainloop()

cursor.close
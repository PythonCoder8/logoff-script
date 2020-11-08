#Automatic Logout Script
#Author: PythonCoder8

import tkinter as tk, time, os

time.sleep(10)
win = tk.Tk()
win.iconbitmap('D:\icon-warning.ico')
win.geometry("700x150")
win.configure(bg="yellow")
win.title("AUTOMATIC LOGOFF")
warnLabelOne = tk.Label(win, text ='WARNING: YOU WILL BE LOGGED OUT IN 10 SECONDS',font=("Arial bold", 18),fg="red",bg="yellow")
warnLabelTwo = tk.Label(win, text='PLEASE SAVE ANY OPENED FILES',font=("Arial bold", 18),fg="red",bg="yellow")
warnLabelOne.pack()
warnLabelTwo.pack()
win.after(5000, lambda: win.destroy())
win.mainloop()
time.sleep(5)
os.system("shutdown -l")
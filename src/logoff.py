#Automatic Logout Script
#Author: PythonCoder8, Cybergavin

import tkinter as tk, time, os

time.sleep(1795)
win = tk.Tk()
win.iconbitmap('C:\icon-warning.ico')
win.geometry("700x150")
win.configure(bg="yellow")
win.title("WARNING")
warnLabelOne = tk.Label(win, text ='WARNING: YOU WILL BE LOGGED OUT IN 60 SECONDS',font=("Arial bold", 18),fg="red")
warnLabelTwo = tk.Label(win, text='PLEASE SAVE ANY OPENED FILES',font=("Arial bold", 18),fg="red")
warnLabelOne.pack()
warnLabelTwo.pack()
win.after(5000, lambda: win.destroy())
win.mainloop()
time.sleep(60)
os.system("shutdown -l")

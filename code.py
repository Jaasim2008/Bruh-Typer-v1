from tkinter import *
from pynput.keyboard import Key, Controller
import time

root = Tk()
root.title('Bruh Typer v1')
root.geometry('400x400')
root.config(bg='#3d3d3d')


def start_type():
    kb = Controller()
    time.sleep(5)
    for x in range(100):
        time.sleep(.01)
        for char in 'Bruh':
            kb.press(char)
            kb.release(char)
            time.sleep(0.12)


btn1 = Button(root, fg='white', bg='#3d3d3d', text='start type (5 secs)', relief=SUNKEN, bd=0,
              font=('Arial Italic', 20), command=start_type)
btn1.pack(pady=20)

btn2 = Button(root, fg='orange', bg='#3d3d3d', text='Close', relief=SUNKEN, bd=0,
              font=('Arial Italic', 20), command=root.destroy)
btn2.pack(pady=20)

root.mainloop()

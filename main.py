# Source Generated with Decompyle++
# File: main.pyc (Python 3.10)

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from random import *
import random
root = tk.Tk()
root['bg'] = 'black'
root.title('Die Roller')
root.geometry('1280x720+50+50')
root.resizable(False, False)
root.iconbitmap('die.ico')
root.configure('black', **('background',))
banner = ImageTk.PhotoImage(Image.open('banner.png'))
test1 = ImageTk.PhotoImage(Image.open('faces/1.png'))
test2 = ImageTk.PhotoImage(Image.open('faces/2.png'))
test3 = ImageTk.PhotoImage(Image.open('faces/3.png'))
test4 = ImageTk.PhotoImage(Image.open('faces/4.png'))
test5 = ImageTk.PhotoImage(Image.open('faces/5.png'))
test6 = ImageTk.PhotoImage(Image.open('faces/6.png'))
panel = tk.Label(root, banner, 'black', **('image', 'bg'))
panel.pack('bottom', 'both', 'yes', **('side', 'fill', 'expand'))
choices = [
    test1,
    test2,
    test3,
    test4,
    test5,
    test6]

def callback(e):
    x = random.randint(0, 5)
    img2 = choices[x]
    panel.configure(img2, **('image',))
    panel.image = img2

root.bind('<space>', callback)
root.mainloop()

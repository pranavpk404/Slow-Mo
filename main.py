import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from tkinter import Menu
from tkinter import filedialog
from tkinter.messagebox import showerror

import PIL.Image
import PIL.ImageTk
import cv2
import imutils
from ttkthemes import ThemedStyle

# BASIC
SET_WIDTH = 650
SET_HEIGHT = 368
root = tk.Tk()
style = ThemedStyle(root)
style.set_theme("keramik")
root.title("Slow Mo")
try:
    root.iconbitmap("Files\\icon.ico")
except Exception as e:
    print(e)
    showerror("error", "You must have deleted the Icon")
    pass

root.config(bg="black")
###########################################################
canvas = tk.Canvas(root, width=SET_WIDTH, height=SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("Files\\welcome.png"), cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.pack()


def browse():
    stream = cv2.VideoCapture(filedialog.askopenfilename())


stream = cv2.VideoCapture(filedialog.askopenfilename())


def play(speed):
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tk.NW)


ttk.Button(root, command=browse, text="<< Browse For file").pack(fill="x")
ttk.Button(root, command=partial(play, -25), text="<< Previous(fast)").pack(fill="x")
ttk.Button(root, command=partial(play, -2), text="<< Previous(slow)").pack(fill="x")
ttk.Button(root, command=partial(play, 2), text="<<Next (slow)").pack(fill="x")
ttk.Button(root, command=partial(play, 25), text="<< Next (fast)").pack(fill="x")


def default_theme():
    style.set_theme("keramik")


def elegance_theme():
    style.set_theme("elegance")


def clear_looks_theme():
    style.set_theme("clearlooks")


def adapta_theme():
    style.set_theme("adapta")


def aquativo_theme():
    style.set_theme("aquativo")


def arc_theme():
    style.set_theme("arc")


def blue_theme():
    style.set_theme("blue")


def black_theme():
    style.set_theme("black")


def breeze_theme():
    style.set_theme("breeze")


def equilux_theme():
    style.set_theme("equilux")


def ITFT1_theme():
    style.set_theme("itft1")


def kroc_theme():
    style.set_theme("kroc")


def plastik_theme():
    style.set_theme("plastik")


menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Change Theme", menu=subMenu)
subMenu.add_command(label="Keramik(Default)", command=default_theme)
subMenu.add_separator()
subMenu.add_command(label="Clearlooks", command=clear_looks_theme)
subMenu.add_command(label="Adapta", command=adapta_theme)
subMenu.add_command(label="Aquativo", command=aquativo_theme)
subMenu.add_command(label="Arc", command=arc_theme)
subMenu.add_command(label="Blue", command=blue_theme)
subMenu.add_command(label="Black", command=black_theme)
subMenu.add_command(label="Breeze", command=breeze_theme)
subMenu.add_command(label="Equilux", command=equilux_theme)
subMenu.add_command(label="ITFT1", command=ITFT1_theme)
subMenu.add_command(label="Elegance", command=elegance_theme)
subMenu.add_command(label="Kroc", command=kroc_theme)
subMenu.add_command(label="Plastik", command=plastik_theme)
root.mainloop()

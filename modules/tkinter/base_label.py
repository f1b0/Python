#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-


from tkinter import *


def create_label():
    # constants
    background_color = 'grey'
    font = "none 14 bold"

    window = Tk()
    window.geometry("60x60+250+250")
    window.title('A Tkinter Label')
    window.configure(background=background_color)

    # label
    label = Label(window, text="A label", bg=background_color, font=font)
    label.grid(row=0)

    window.mainloop()

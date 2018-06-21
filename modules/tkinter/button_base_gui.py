#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-


from tkinter import *


main_window = Tk()


def button_hello():
    return "Hello there!"


button = Button(main_window, text="Button 1", font="none 14 bold", command=)
button.pack()

main_window.geometry("300x200+250+250")
main_window.mainloop()

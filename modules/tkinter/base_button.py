#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-


from tkinter import *


def create_button():
    window = Tk()
    window.geometry("50x50+250+250")
    window.title('Tkinter Button')
    window.configure(background='grey')

    def hello():
        print("Hello there!")

    def close():
        window.destroy()

    button_hello = Button(window, text="hello", font="none 14 bold", command=hello)
    button_quit = Button(window, text="quit", font="none 14 bold", command=close)
    button_hello.grid(row=0)
    button_quit.grid(row=1)
    window.mainloop()

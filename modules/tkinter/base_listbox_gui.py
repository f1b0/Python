#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-


from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()

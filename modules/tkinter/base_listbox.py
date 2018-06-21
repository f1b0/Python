#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-

from tkinter import *

# config variables #
background_color = 'grey'
font = 'none 14'


def on_select(evt):
    w = evt.widget
    line_nr = int(w.curselection()[0])
    line_value = w.get(line_nr)
    print(line_nr, line_value)


# window #
main_window = Tk()
main_window.geometry("182x250+250+250")                 # width, height
main_window.title('Tkinter ListBox')
main_window.configure(background=background_color)

# List box #
# label
label = Label(main_window, text="A ListBox", bg=background_color, font=font)
# list box
listbox = Listbox(main_window)
listbox.bind('<<ListboxSelect>>', on_select)
listbox.insert(END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

# Layout #
label.grid(row=0, column=0, sticky=N + S + E + W)
listbox.grid(row=1, column=0, sticky=N+S+E+W)


main_window.mainloop()


#!/Users/f1b0/anaconda3/bin/python3.6


# import tkinter as tk #
from tkinter import *

# config varables #
background_color = 'grey'
font = 'none 14'


def button_hello():
    print(input_text.get())


# window #
main_window = Tk()
input_text = StringVar()
main_window.geometry("182x250+250+250")                 # width, height
main_window.title('SSH Manager')
main_window.configure(background=background_color)

# Text Input with button
# Label #

# Text Field #
# text_field = Entry(main_window, textvariable=input_text)
# Buttons #
# button = Button(main_window, text="Button 1", font="none 14 bold", command=button_hello)

# List box #
# label
label_host_list = Label(main_window, text="Host List", bg=background_color, font=font)
# list box
listbox = Listbox(main_window)
listbox.insert(END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

# Layout #
label_host_list.grid(row=0, column=0, sticky=N+S+E+W)
# text_field.grid(row=1, column=1)
# button.grid(row=1, column=2)
listbox.grid(row=1, column=0, sticky=N+S+E+W)

# Layout Window #
# run
main_window.mainloop()


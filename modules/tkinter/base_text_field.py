#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-


from tkinter import *


def create_textfield():
    # constants
    background_color = 'grey'
    font = "none 14 bold"

    window = Tk()
    text_input = StringVar()
    window.geometry("215x250+100+100")
    window.title('A Tkinter Text Field')
    window.configure(background=background_color)

    # text field
    textfield = Entry(window, textvariable=text_input, bg='white', font=font)
    textfield.grid(row=0, sticky=S+N)

    def get_text():
        output = 'Your input was:\n\n{}'.format(text_input.get())
        return output

    def replace_text_field():
        text_output_area = Text(window, bg='white', font=font, height=10)
        text_output_area.insert(INSERT, get_text())
        text_output_area.grid(row=1, sticky=S + N + W + E)
        return str(text_input.get())

    # Button
    button_print = Button(window, text="PRINT", font="none 14 bold", command=replace_text_field)
    button_print.grid(row=2, sticky=S+N)

    window.mainloop()
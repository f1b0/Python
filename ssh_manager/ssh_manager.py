#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-

from tkinter import *
import csv
import os
import getpass


class SSHManagerGui(object):
    def __init__(self, window_geometry, font, background_color):
        self.font = font
        self.selected_item = []
        self.bgcolor = background_color
        self.window_geo = window_geometry
        self.main_window = Tk()
        self.main_window.geometry(self.window_geo)
        self.main_window.title('SSH Manager')
        self.main_window.configure(background=self.bgcolor)

        # labels
        self.label_host_list = Label(self.main_window, text="Host List", bg=self.bgcolor, font=font)
        # List box #
        self.listbox = Listbox(self.main_window, name='host_list', bg=self.bgcolor, height=10, width=25)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.listbox.scrollbar = Scrollbar(self.listbox, orient=VERTICAL)
        self.listbox.config(yscrollcommand=self.listbox.scrollbar)
        self.listbox.scrollbar.config(command=self.listbox.yview)

        # Buttons
        self.connect_button = Button(self.main_window, text="connect", font=self.font, command=self.open_new_terminal)
        self.quit_button = Button(self.main_window, text="quit", font=self.font, command=self.close_window)

        # Layout #
        self.label_host_list.grid(row=0, column=0, columnspan=1, sticky=N + S + E + W)
        self.listbox.grid(row=1, column=0, columnspan=1, sticky=N + S + E + W)
        self.connect_button.grid(row=2, column=0, columnspan=1, sticky=N + S + E + W)
        self.quit_button.grid(row=3, column=0, columnspan=1, sticky=N + S + E + W)

    def load_host_list(self, entry_list):
        self.listbox.insert(END, entry_list)

    def on_select(self, evt):
        w = evt.widget
        line_nr = int(w.curselection()[0])
        line_value = w.get(line_nr)
        self.selected_item.append(str(line_value[0][0]))    # host
        self.selected_item.append(str(line_value[1][0]))    # username
        self.selected_item.append(str(line_value[2][0]))    # password

    @staticmethod
    def read_csv_file(csv_file, delimiter):
        host_list = []
        user_list = []
        pwd_list = []
        with open(csv_file, 'r') as csvfile:
            for row in csv.reader(csvfile, delimiter=delimiter):
                host_list.append(row[0])
                user_list.append(row[1])
                pwd_list.append(row[2])
        csvfile.close()
        return [host_list, user_list, pwd_list]

    def open_new_terminal(self):
        template = '/Users/f1b0/Workspace/tools/ssh_manager/open_terminal_base.sh'
        script = '/Users/f1b0/Workspace/tools/ssh_manager/open_terminal.sh'
        print(self.selected_item)
        host = self.selected_item[0]
        user = self.selected_item[1]
        pwd = self.selected_item[2]
        # Read in the file
        with open(template, 'r') as file:
            filedata = file.read()
            file.close()
        # Replace the target string
        filedata = filedata.replace('_HOST_', host)
        filedata = filedata.replace('_USERNAME_', getpass.getuser())

        # Write the file out again
        with open(script, 'w') as file:
            file.write(filedata)
            file.close()
        del self.selected_item[:]
        os.system('/bin/bash -e ' + script)

    def close_window(self):
        self.main_window.destroy()

    def start(self):
        # run
        self.main_window.mainloop()


def write_bash_script(host, user):
    template = '/Users/f1b0/Workspace/tools/ssh_manager/open_terminal_base.sh'
    script = '/Users/f1b0/Workspace/tools/ssh_manager/open_terminal.sh'
    # Read in the file
    with open(template, 'r') as file:
        filedata = file.read()
        file.close()

    # Replace the target string
    filedata = filedata.replace('_HOST_', host)
    filedata = filedata.replace('_USERNAME_', user)

    # Write the file out again
    with open(script, 'w') as file:
        file.write(filedata)
        file.close()


def create_window():
    # config variables
    background_color = 'grey'
    font = 'none 14'
    window_geometry = "400x400+250+250" # width, height
    csv_file = '/Users/f1b0/Workspace/tools/ssh_manager/host_list.csv'

    mgr = SSHManagerGui(window_geometry, font, background_color)
    connection_lst = mgr.read_csv_file(csv_file, ';')
    mgr.load_host_list(connection_lst)

    mgr.start()


if __name__ in '__main__':
    create_window()

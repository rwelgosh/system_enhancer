#!/usr/bin/env python3
import os
from tkinter import *
from tkinter.ttk import *
import system_check
import delete_directory
import sort_files

screen = Tk()
screen.title("System Enhancer")
screen.geometry("1000x500")

keys = []
file_location = os.path.join(os.path.dirname(__file__), "Keys.txt")

file_key_var = StringVar()
folder_name_var = StringVar()

def import_keys(file_location):
    with open(file_location) as file:
        for line in file:
            keys.append(line.strip())

def manage_k():
    manage_screen = Toplevel(screen)
    manage_screen.title("Manage Keys")
    manage_screen.geometry("500x500")

    print(keys)

    print("managing")

def add_k():
    add_screen = Toplevel(screen)
    add_screen.title("Add Keys")
    add_screen.geometry("500x500")

    Label(add_screen, text="File Key").grid(row=0, column=2)
    Label(add_screen, text="Folder Name").grid(row=1, column=2)

    file_key = Entry(add_screen, textvariable = file_key_var, width=50)
    folder_name = Entry(add_screen, textvariable = folder_name_var, width=50)
    file_key.grid(row=0, column=3)
    folder_name.grid(row=1, column=3)

    add_key = Button(add_screen, text="Submit", command = submit_key)
    add_key.grid(row=2, column=2)

    import_keys(file_location)

    print("Adding")

def submit_key():
    f_k = file_key_var.get()
    f_n = folder_name_var.get()

    with open(file_location, "a") as file:
        file.write(str(f_k) + "_" + " :: " + str(f_n) + "\n")

    file_key_var.set("")
    folder_name_var.set("")

import_keys(file_location)

manage_keys = Button(screen, text="Manage Keys", width=25, command=manage_k).grid(row=0, column=5)
add_keys = Button(screen, text="Add Keys", width=25, command=add_k).grid(row=1, column = 5)

screen.mainloop()

#!/usr/bin/env python3
import tkinter as tk
import sort_files
import delete_directory

def manage_k():
    print("managing")

def add_k():
    print("Adding")

screen = tk.Tk()
screen.title("System Enhancer")
screen.geometry("500x500")

manage_keys = tk.Button(screen, text="Manage Keys", width=25, command=manage_k)
add_keys = tk.Button(screen, text="Add Keys", width=25, command=add_k)

manage_keys.pack()
add_keys.pack()
screen.mainloop()

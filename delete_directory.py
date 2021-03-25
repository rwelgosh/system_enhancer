#!/usr/bin/env python3
import os
import ctypes
import sys

curdir = os.getcwd()

def recursive_delete(dir):

    os.chdir(dir)
    curdir = os.getcwd()
    subdir = os.listdir(curdir)
    for i in range(len(subdir)):
        fullname = os.path.join(curdir, subdir[i])
        if os.path.isdir(fullname):
            recursive_delete(fullname)
            if len(os.listdir(fullname)) == 0:
                os.rmdir(fullname)
            else:
                print("File isn't empty")
        else:
            os.remove(fullname)
    name = os.path.join(os.getcwd(), os.pardir)
    os.chdir(name)

def delete_directory():
    subdir = os.listdir(curdir)
    print("Which directory would you like to delete?")
    for i in range(len(subdir)):
        print(str(i) + ": " + subdir[i])
    toDelete = input()
    deletedir = ""
    for i in range(len(subdir)):
        if int(toDelete) == i or toDelete == subdir[i]:
            print(i)
            deletedir = os.path.join(curdir, subdir[i])

    print("Are you sure you want to delte \"" + deletedir + "\"? (you will be deleting all directories and files within this directory) y/n")
    confirmation = input()
    if confirmation == "y" or confirmation == "Y":
        recursive_delete(deletedir)

        os.rmdir(deletedir)
    else:
        print("Will not delete any folders")
        return


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    delete_directory()
else:
     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

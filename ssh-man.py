#!/usr/bin/env python
import pathlib
import os
import pickle
import subprocess
import shlex

# Check if save file exists and create it if not
savefiledir = f"{pathlib.Path.home()}/.config/ssh-man"
savefile = f"{savefiledir}/saves.pkl"
if os.path.exists(savefiledir):
    if os.path.getsize(savefile) > 0:
        with open(savefile, "rb") as f:
            saves = pickle.load(f)
    else:
        saves = []  # create empty list
else:
    os.mkdir(savefiledir)  # create file and directory
    os.mknod(savefile)
    saves = []

while True:
    print("Welcome to Ohas shitty SSH-Man. What do you wanna do?\n[1] Add a new connection\n[2] View saved connections\n[3] Remove saved connection")
    sel = int(input())

    if sel == 1:
        name = input("Name of the connection: ")
        user = input("Your username: ")
        host = input("Hostname of the remote server: ")
        saves.append([name, user, host])
        with open(savefile, "wb") as f:
            pickle.dump(saves, f)
        print("Connection saved to connection list.")
    elif sel == 2:
        a = 0
        if not saves:
            print("No saved connections.")
        else:
            print("Saved connections:")
            for i in saves:
                a = a + 1
                print(f"- [{a}] {i[0]}")
            conn = int(input("Which connection would you like to connect to?"))
            conn -= 1
            if 0 <= conn < len(saves):
                os.system(f"ssh {saves[conn][1]}@{saves[conn][2]}")
            else:
                print("Invalid connection number.")

    elif sel ==3:
        print("Saved connections:")
        a = 0
        for i in saves:
            a = a + 1
            print(f"- [{a}] {i[0]}")
        conn = int(input("Which connection would you like to remove?"))
        conn -= 1
        if 0 <= conn < len(saves):
            choice = input(f"Do you really want to remove {saves[conn][0]}? [y/n]")
            if choice == "y":
                saves.pop(conn)
                with open(savefile, "wb") as f:
                    pickle.dump(saves, f)
            elif choice == "n":
                continue
            else:
                print("Invalid Input. Use y or n")
        else:
            print("Invalid connection number.")
    else:
        print("Invalid/Not implemented function.")
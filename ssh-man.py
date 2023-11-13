import pathlib
import os
savefiledir = f"{pathlib.Path.home()}/.config/ssh-man"
saves = []
while True:
    print("Welcome to Ohas shitty SSH-Man. What do you wanna do? \r\n [1] Add a new connection \r\n [2] View saved connections")
    sel = int(input())
    if sel == 1:
        name = input("Name of the connection: ")
        user = input("Your username: ")
        host = input("Hostname of the remote server: ")
        saves.append([name, user, host])
        print(saves)
    elif sel == 2:
        a = 0
        print("Saved connections: ")
        for i in saves:
            a = a +1
            print(f"- [{a}] {i[0]}")
        conn = int(input("Which connection would you like to connect to?"))
        conn = conn - 1
        os.system(f"konsole -e ssh {saves[conn][1]}@{saves[conn][2]}")

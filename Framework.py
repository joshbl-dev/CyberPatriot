from __future__ import print_function
from passlib.hash import pbkdf2_sha256
import os, sys, time, subprocess, LinuxScript, getpass

def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    elif sys.platform.startswith('linux'):
        subprocess.Popen("clear", shell=True)

def frameworkStartup():
    symbols = ["}","/", "\\", "|"]
    colors = ["38;5;39", "37"]#[cyan, white,]
    clearScreen()
    # prints Cyber Patriot to console
    textfile = open("CyberPatriot.txt", "r")
    for line in textfile.readlines():
        character = list(line)
        for i in range(len(character)):
            if character[i] in symbols:
                charColor = colors[0]
            else:
                charColor = colors[1]
            print("\033[" + charColor + "m" + character[i], end="", flush=True)
            time.sleep(0.005)
    print()

def enterCommand():
    # Wait for command
    time.sleep(1)
    print("\n\n"+"\033[39m"+"Command: ", end="")
    command = input()
    return command

def doCommand(command):

    possiblecmds = dir(LinuxScript)
    notcmds = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
    for i in range(len(notcmds)):
        if notcmds[i] in possiblecmds:
            possiblecmds.remove(notcmds[i])

    if command.lower() == "exit":
        print("Goodbye user.")
        return False
    elif command.lower() == "help":
        modules = open("modules.txt", "r")
        for line in modules.readlines():
            print(line, end="")
    elif command.lower() == "restart":
        frameworkStartup()
    elif command.lower() == "linuxcmds":
        for i in range(len(possiblecmds)):
            num = i+1
            print(str(num)+". " + possiblecmds[i])
    elif command == "allowPort":
        LinuxScript.allowPort()
    elif command == "auditLogs":
        LinuxScript.auditLogs()
    else:
        print("That is not a valid command. Please contact the developer for any questions/concerns.")

def verify():
    count = 0
    status = True
    while (count <4):
        if status == False:
            print("Invalid Password")
        file = open("passwords.txt", "r")
        hashes = file.readlines()
        password = getpass.getpass()
        for i in range(len(hashes)):
            status = pbkdf2_sha256.verify(password, hashes[i].strip())
            if status:
                print("Accepted.")
                count = 999
                break
        count += 1
        if count == 3:
            print("Password limit reached. Goodbye.")
            exit(1)

def main():
    os.system("title CyberPatriot Framework")
    clearScreen()
    info = open("info.txt", "r")
    for line in info.readlines():
        print("\033[39m" + line)
    os.system("pause")
    clearScreen()
    verify()
    print("Initializing in...")
    for i in range(3):
        print(3 -  i)
        time.sleep(1)
    frameworkStartup()
    while True:
        action = enterCommand()
        status = doCommand(action)
        if status == False:
            break

if __name__ == '__main__':
    main()
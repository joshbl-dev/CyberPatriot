from __future__ import print_function
import os, sys, time, random as r, subprocess

def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    elif sys.platform.startswith('linux'):
        subprocess.Popen("clear", shell=True)

def startup():
    colors = ["31","34", "35", "36", "91","94", "95", "96", "97", "39"]

    print("Please make the terminal full screen...Starting in...")
    for i in range(5):
        print(5 - i)
        time.sleep(1)

    clearScreen()

    # prints Cyber Patriot to console
    textfile = open("CyberPatriot.txt", "r")
    for line in textfile.readlines():
        character = list(line)
        for i in range(len(character)):
            charColor = colors[r.randrange(0, len(colors))]
            print("\033[" + charColor + "m" + character[i], end="")
            time.sleep(0.01)

def command():
    # Wait for command
    time.sleep(1)
    print("\n\n\n\033[39mWelcome to the framework!")
    print("We are waiting for your next command! Impress us!\nCommand: ", end="")
    command = input()


def main():
    clearScreen()
    startup()
    command()


if __name__ == '__main__':
    main()
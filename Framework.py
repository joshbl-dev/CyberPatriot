from __future__ import print_function
import os
import time
import random as r

def startup():
    colors = ["31", "32", "33", "34", "35", "36", "91", "92", "93", "94", "95", "96", "97", "30", "39"]

    print("Please make the terminal full screen...Starting in...")
    for i in range(5):
        print(5 - i)
        time.sleep(1)
    os.system("clear")

    # prints Cyber Patriot to console
    textfile = open("CyberPatriot.txt", "r")
    for line in textfile.readlines():
        character = list(line)
        for i in range(len(character)):
            time.sleep(0.01)
            charColor = colors[r.randrange(0, 15)]
            # if i % 10 == 0:
            # subprocess.Popen(charColor, shell=True)
            print("\033[" + charColor + "m" + character[i], end="")


def command():
    # Wait for command
    time.sleep(1)
    print("\n\n\n\033[39mWelcome to the framework!")
    print("We are waiting for your next command! Impress us!\nCommand: ", end="")
    command = input()


def main():
    startup()
    command()


if __name__ == '__main__':
    main()
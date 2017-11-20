from passlib.hash import pbkdf2_sha256
from tkinter import *

def enter(entry):
    password = e1.get()
    master.destroy()
    hash(password)

def verify():
    count = 0
    status = True
    while (count <4):
        if status == False:
            print("Invalid Password")
        file = open("passwords.txt", "r")
        hashes = file.readlines()
        print("Authorized user: ", end="", flush=True)
        password = input()
        for i in range(len(hashes)):
            status = pbkdf2_sha256.verify(password, hashes[3].strip())
            if status:
                print("Accepted.")
                count = 999
                break
        count += 1
        if count == 3:
            print("Password limit reached. Goodbye.")
            exit(1)

def hash(password):
    hash = pbkdf2_sha256.hash(password)
    verify()
    passwords = open("passwords.txt", "a")
    passwords.write("\n" + hash)
    passwords.close()
    print("Your password has been successfully hashed. Goodbye.")
    exit()

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

master = Tk()
master.title("Password")
center(master)
master.geometry('{}x{}'.format(200, 25))
master.resizable(width=False, height=False)
Label(master, text="Password: ").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
e1.bind("<Return>", enter)
mainloop()


from tkinter import *
# pip install pyperclip
import pyperclip
import random

root = Tk()
root.geometry("700x300")
root.config(background="black")
passwrd = StringVar()

passlen = IntVar()
passlen.set(0)


def generate():  # Function to generate the password
    pass1 =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z']
    pass2=[' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')','1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

        password = password + random.choice(pass2)
    passwrd.set(password)

def accept():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
    root.destroy()

def reset():
    generate()

Label(root, text="Strong Password Generator",font=50,bg='maroon').pack()
Label(root,text="Enter name").pack(pady=1)
Entry(root).pack(pady=2)
Label(root, text="Enter the number to get password").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Tap to get", command=generate,background="green").pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="ACCEPT", command=accept,background="green").pack()
Button(root,text="RESET",command=reset,background="green").pack()
root.mainloop()

















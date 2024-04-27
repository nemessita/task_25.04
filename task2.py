# 2 Proqram soruşur:

# 	 Yeni ad (1) Adi sil (2) Adi redakte et(3) Fayli silin (4):  

# Qeyd:

#  Bazada hec bir ad yoxdur ilk adi siz daxil edin
#  Bazada 5 ad var
#  Siz ad daxil etmediniz
#  Ad artiq bazada movcuddur

import os

def new_word():
    add = input("yeni ad elave edin: ")
    with open("file.txt", "a") as file:
        file.write(add + "\n")

def delete_word():
    word_to_delete = input("silmek isdediyniz soz: ")
    lines = []
    with open("file.txt", "r") as file:
        lines = file.readlines()
    with open("file.txt", "w") as file:
        for line in lines:
            if line.strip() != word_to_delete:
                file.write(line)
    print("ugurla silindi.")

def edit_word():
    old_word = input("hazirki soz: ")
    new_word = input("deyismek isdediyniz yeni soz: ")
    with open("file.txt", "r") as file:
        lines = file.readlines()
    with open("file.txt", "w") as file:
        for line in lines:
            if line.strip() == old_word:
                file.write(new_word + "\n")
            else:
                file.write(line)
    print("ugurla deyisildi.")

def delete_file():
    if os.path.exists("file.txt"):
        os.remove("file.txt")
        print("File ugurla silindi.")
    else:
        print("File silinmedi_xetani tap!!!.")

def cread():
    while True:
        choice = input("Yeni ad (1) Adi sil (2) Adi redakte et(3) Fayli silin (4)  cixis (5):  ")
        if choice == "1":
            new_word()
        elif choice == "2":
            delete_word()
        elif choice == "3":
            edit_word()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            exit()
        else:
            print("yalnis secim.")

cread()

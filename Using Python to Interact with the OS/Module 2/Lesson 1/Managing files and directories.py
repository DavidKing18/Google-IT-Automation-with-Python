''' LESSON 1 - Reading Files'''
file = open("C:/Users/DAVID\Documents/My files\Coursera/Using Python to Interact with the OS/Module 2/spider.txt")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
print()

with open("spider.txt") as file:
    print(file.read())
print()

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
print()

file = open("spider.txt")
lines = file.readlines()
file.close()
print(lines)
print()



''' LESSON 2 - WRITING FILES'''

with open("rabbit.txt", "w") as file:
    file.write("Little lads lost some lambs.\n")
with open("rabbit.txt") as file:
    print(file.read())

with open("rabbit.txt", "a") as file:
    file.write("Take this note and shut it!!!")
with open("rabbit.txt") as file:
    print(file.read())



''' LESSON 3 - MANAGING FILES AND DIRECTORIES'''

import os
os.remove('rabbit.txt')
os.rename("spider.txt", "orangutan.txt")
os.path.exists("orangutan.txt")
os.path.getsize("orangutan.txt")
os.path.getmtime("Orangutan.txt")
print()
with open("rabbit.txt", "w") as file:
    file.write("Music is sound that is pleasand to the hear.\nNoise is an obstruction to concentratin.\nMeditation is important in Yoga. ")
with open("spider.txt", "w") as file:
    file.write("Music is sound that is pleasand to the hear.\nNoise is an obstruction to concentratin.\nMeditation is important in Yoga. ")

import datetime
timestamp = os.path.getmtime("orangutan.txt")
print(datetime.datetime.fromtimestamp(timestamp))
os.remove("orangutan.txt")
print()


os.path.abspath("managing\ files\ and\ directories.py")

os.getcwd()
os.mkdir("new_dir")
os.rmdir("new_dir")
os.chdir(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.path.join(os.getcwd(), "Managing files and directories.py"))
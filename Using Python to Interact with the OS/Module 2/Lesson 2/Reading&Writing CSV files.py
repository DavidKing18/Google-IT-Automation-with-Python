#!/usr/bin/env python3

import csv
file = open("csv_file.txt")
csv_file = csv.reader(file)
for row in csv_file:
    name, phone, role = row
    print("Name: {:<16}  |  Phone: {:<12}  |  Role: {}".format(name, phone, role))
print()

position = [['Olusegun Adeleke', ' 802-323-4002', ' System Administrator'], ['Olawumi Adeleke', ' 803-073-1983', ' Counselor'], ['David Adeleke', ' 808-360-3251', ' IT Specialist '], ['Adeola Adeleke', ' 902-499-8344', ' UI/UX Designer']]
with open("Position.csv", "w") as csv_file:
    fileWrite = csv.writer(csv_file)
    fileWrite.writerows(position)
print()

with open("C:/Users/DAVID/Documents/My files/Coursera/Using Python to Interact with the OS/Module 2/Lesson 2/software.txt") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has{} users.".format(row["name"], row["user"]))
print()

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "UX Reasearch"}, 
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as by_department:
   writer = csv.DictWriter(by_department, fieldnames = keys)
   writer.writeheader()
   writer.writerows(users)

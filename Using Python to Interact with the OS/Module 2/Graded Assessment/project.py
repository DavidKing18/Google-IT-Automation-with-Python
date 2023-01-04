'''
    Introduction
For this assessment, imagine you are an IT Specialist at a medium-sized company. The Human Resources Department at your company wants you to find out how many people are in each department. You need to write a Python script that reads a CSV file containing a list of the employees in the organization, counts how many people are in each department, and then generates a report using this information. The output of this script will be a plain text file.
'''

import os
import csv
def read_employees(csv_file_location):
    with open(csv_file_location) as file:
            csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
            employee_file = csv.DictReader(file, dialect = "empDialect")
            employee_list = []
            for data in employee_file:
                    employee_list.append(data)
    return employee_list

employee_list = read_employees('employees.txt')
print("TEST OUTPUT 1:\n")
print(employee_list)
print('\n\n')

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data["Department"])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)
print("TEST OUTPUT 2:\n")
print(dictionary)
print()


def write_report(dictionary, report_file):
        with open(report_file, 'w+') as file:
                for k in sorted(dictionary):
                        file.write(str(k)+": "+str(dictionary[k])+"\n")
                file.close()

write_report(dictionary, "test_report.txt")


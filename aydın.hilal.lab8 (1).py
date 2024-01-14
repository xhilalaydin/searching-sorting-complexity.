# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:51:35 2023

@author: hilala-ug
"""

from Birthday import Birthday

def read_birthdays(file):
    file = open("birthdays.txt" , "r")
    birtdayObj = []
    for line in file:
        data = line.strip().split(";")
        #name, month,day = data[0],int(data[1]),int(data[2])
        birthdays = Birthday(data[0],int(data[1]),int(data[2]))
        if birthdays  in birtdayObj:
            print(f"{data[0]} is already in the list")
        else:
            birtdayObj.append(birthdays)
    return birtdayObj

def selection_sort(birthdayObj):
    ind = 0
    while ind != len(birthdayObj):
        for i in range(ind ,len(birthdayObj)):
            if birthdayObj[i] < birthdayObj[ind]:
                birthdayObj[i], birthdayObj[ind] =  birthdayObj[ind], birthdayObj[i]
        ind += 1    
    
def binary_search(sorted_list , name):
    if len(sorted_list) == 0:
        return None
    if sorted_list[len(sorted_list)-1].getName() == name:
        return sorted_list[len(sorted_list)-1] 
    else:
        sorted_list.pop()
        return binary_search(sorted_list, name)
    
def linear_search(birtdayObj, month ,day):
    listo = []
    for elm in birtdayObj:
        if elm.getMonth() == month and elm.getDay()== day:
            listo.append(elm.getName())
    return listo 

file = "birthdays.txt"
birthday_list = read_birthdays(file)
month_input= (int(input("Enter the month: ")))
day_input = (int(input("Enter the day: ")))
matching_names = linear_search(birthday_list, month_input, day_input)
print(f"People born on the same day : {matching_names}" if matching_names else "No birthday on that day!")

selection_sort(birthday_list)
print("Sorted List:")
for birthday in birthday_list:
    print (f"{birthday.getName()}: {birthday.getMonth()}/{birthday.getDay()}")
    
    
   
name =input("Enter name to search: ")
dateOf = binary_search(birthday_list, name)
print(dateOf)



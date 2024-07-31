#!/usr/bin/env python
#Jasmin
#07/10/2024
# This code print depends of what will be input
username = input("Login: >> ")
user1 = "Jack"
user2 = "Jill"
if username == user1: # if input was "Jack" it is gonna print next
    print("Access granted") 
elif username == user2: # if input was "Jill" it is gonna print next
    print("Welcome to the system") 
else:   # if there is different input ot is gonna print next
    print("Access denied")

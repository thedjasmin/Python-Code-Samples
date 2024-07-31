# Jasmin Duishebaeva
# 07.22.2024
# Problem 7 - It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. 
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you 
# would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day 
# number, and the length of your stay, and it will tell you the number of day of the week you will return on.
print("0 - Sunday")
print("1 - Monday")
print("2 - Tuesday")
print("3 - Wednesday")
print("4 - Thursday")
print("5 - Friday")
print("6 - Saturday")
start = int(input("Write starting day: "))
nights = int(input("Write how many nights: "))
return_day = (start + nights) % 7
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("You will return on ", days_of_week[return_day])
# Jasmin Duishebaeva
# 08.30.2024
# Problem 3: Using a while loop, ask the user to enter a number. 
# Append each entered number to a list and add them together. 
# Continue asking for a number until the sum of the list ofnumbers is greater than 100.


numbers = []
total = 0

while total <= 100:
    num = float(input("Enter a number: "))
    numbers.append(num)
    total += num

print(numbers)  
print(f"Total sum: {total}")  

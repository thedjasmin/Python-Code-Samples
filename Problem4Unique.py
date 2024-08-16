# Jasmin Duishebaeva
# 08.15.2024

# Problem 4: Write a Python function that takes a list of numbers and returns a new list with unique elements.

def uniqueList(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst

# Example usage
a = int(input("write first number of the list: "))
b = int(input("write second number of the list: "))
c = int(input("write third number of the list: "))
d = int(input("write fourth number of the list: "))
numbers = [a, b, c, d]
print("The unique elements in the list are", uniqueList(numbers))

# Jasmin Duishebaeva
# 08.15.2024

# Problem 3: Write a Python function to multiply all the numbers in a list.

def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
a = int(input("write first number of the list: "))
b = int(input("write second number of the list: "))
c = int(input("write third number of the list: "))
d = int(input("write fourth number of the list: "))
numbers = [a, b, c, d]
print("The result of multiplying all the numbers in the list is", multiplyList(numbers))

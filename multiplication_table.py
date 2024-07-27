'''
Write a program to print the multiplication table of a given number using a for loop.
'''

def multiplication_table(number):

    for i in range(1, 11):

        print(f"{number} x {i} = {number * i}")

numbers = int(input())
print(multiplication_table(numbers))


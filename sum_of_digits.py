'''
Write a program to find the sum of the digits of a given number using a for loop.
'''
def sum_of_digits(num):
    total = 0
    for digit in num:
        total += int(digit)
    return total

num = input('Enter your digits: ')
result = sum_of_digits(num)
print(f'The sum of the digits of {num} is {result}')

'''
if the elements in an iterable, such as a list, tuple, or set. the sum() function takes two arguments:
1. an iterable containing the number to be summed.
2. an optional start value (default is '0') to be added to the total sum. 
'''

# sum of tuples
number = (1,2,3,4,5,6)
total = sum(number)
print(total)


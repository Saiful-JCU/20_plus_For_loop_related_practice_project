'''
Write a program to find the largest number in a given list using a for loop.
'''

def find_largest(numbers):
    if not numbers:
        return None # Handle the case for an empty list
    largest_number = numbers[0] #initialize with the first element of the list. this is the point for comparisons.
    for number in numbers:
        if number > largest_number: #checks if the current number is greater than the 'largest_number'
            largest_number = number # if true, it updates 'largest_number' with the current number
    return largest_number

numbers = [213,43,6,4,675,75,]
print('the largest number is', find_largest(numbers))





# using max()
list = [1,2,3,4,5,67,7,8,9]
largest = max(list)
print(largest)
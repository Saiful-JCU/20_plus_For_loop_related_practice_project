'''
Write a program to print the first n terms of the Fibonacci series using a for loop, where n is a positive integer
provided by the user.
'''

def fibonacci_sequence(n):
    sequence = []
    a,b = 0, 1 # i initialize a and b to 0 and 1, which are the first two number in the fibonacci sequence.
    for i in range(n):
        sequence.append(a)
        a,b = b, a+b  # i update a to b and b to be a+b (the new fibonacci number)
    return sequence
n = int(input())
print(fibonacci_sequence(n))


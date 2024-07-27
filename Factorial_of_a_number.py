'''
Write a program to calculate the factorial of a given number using a for loop.

# Definition of a Factorial
The factorial of a number is the multiplication of all the numbers between 1 and the number itself. it is written like
this: n!. so the factorial of 3 is 2!=(1*2*3).

'''

f = int(input('write your number: '))
sum = 1 #start with 1 since multiplying by 0 would alwys give 0
for i in range(1, f + 1):
    sum *= i
print(f'The factorial of {f} is {sum}')




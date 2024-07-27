'''
Write a program to check if a given number is prime using a for loop.
'''

def check_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
num = int(input("Enter a number: "))
is_prime = check_prime(num)
if check_prime(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')




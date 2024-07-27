'''
Given a list of numbers, write a program to print all even numbers using a for loop.
'''

n_list =[2 ,3,64,64,3,64,7,4,3,]
even = []
for num in n_list:
    if (num % 2) == 0:
        even.append(num)
print(even)

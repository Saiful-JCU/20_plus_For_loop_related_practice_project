'''
Write a program to reverse a given string using a for loop.
'''

s = input('write any string: ')
final = ''
for char in s:
    final = char + final
print(final)


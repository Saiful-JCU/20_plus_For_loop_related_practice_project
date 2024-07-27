'''
Write a program to count the number of vowels in a given string using a for loop.
'''

str = 'saiful islam khan'
vowels = 'aAeEIioOuU'

count = sum(str.count(vowel) for vowel in vowels)
print(count)

# alternative solution

def vowel_count(string):
    count = 0
    vowels_1 = 'aAeEIioOuU'
    for alph in string:
        if alph in vowels_1:
            count+=1
    return count

string = input('write your words here: ')
print(vowel_count(string))

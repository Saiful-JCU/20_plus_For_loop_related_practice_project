'''
Write a program to count the number of words in a given sentence using a for loop.
'''

def count_word(sentence):
    word_count = 1
    for char in sentence:
        if char == ' ':
            word_count += 1
    return word_count


string = input('write your sentence: ')
print(count_word(string))



# Alternative without for loop

str = 'my name is md saiful islam khan.'
words = str.split()
print(len(words))




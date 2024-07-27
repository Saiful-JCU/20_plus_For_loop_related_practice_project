'''
Given a list of numbers, use a for loop to create a new list that contains the square of each number.
'''

def create_new_list(original_list):
    new_list = []
    for n in original_list:
        squared_num = n ** 2
        new_list.append(squared_num)
    return new_list

original_list = [1,2,3,4,5,6,7,8,9,10]
result = create_new_list(original_list)
print(f'Original list: {original_list}')
print(f'The new list is {result}')





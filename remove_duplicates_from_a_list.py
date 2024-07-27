'''
Write a program to remove duplicate elements from a list using a for loop.
'''

def remove_duplicates(list):
    unique_elements = []
    for element in list:
        if element not  in unique_elements:
            unique_elements.append(element)
    return unique_elements

list = ['saiful', 'niloy', 'milon' ,'saiful', 'arif']
print(remove_duplicates(list))


# Method 2: using a set
# sets automatically remove duplicates because they cannot contain duplicate elements.

def remove_duplicate(n_list):
    list_1 = set(n_list)
    return list_1

n = [1,2,3,1,4,3,5,46,3,5,3]
print(remove_duplicate(n))



'''
Method 3: Using a Dictionary (maintaining Order)
in python 3.7 and later, dictionaries maintain insertion order, so you can use a dictionary to remove duplicates while
maintaining the original ordr:
'''

def remove_duplicates_3(d_list):
    list = dict.fromkeys(d_list)
    return list

ls = ['milon', 'mahi', 'shefaul','milon']
print(remove_duplicates_3(ls))
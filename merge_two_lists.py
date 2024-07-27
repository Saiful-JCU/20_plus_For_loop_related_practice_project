'''
Given two lists, write a program to merge them into a single list using a for loop.
'''

# Method 3: Using list comprehension

ls1 = [1,2,3,4,]
ls2 = [5,6,7]
ls3 = [8,9]
merged_list_1 = []
for sublist in [ls1, ls2, ls3]:
    for item in sublist:
        merged_list_1.append(item)
print(merged_list_1)

'''
Method 2: Using the '+' Operator
'''

ls4 = [11,22,33,44,55]
ls5 = [66,77,88]
ls6 = [99,00]

m_list = ls4 + ls5 + ls6
print(m_list)

'''Method 3: Using the 'extend()' Method -- the extend() method adds elements of one list to the end of another list.'''

ls7 = [11,22,33,44,55]
ls8 = [66,77,88]
ls9 = [99,00]
me_list = ls7.copy() # create a copy to avoid modifying the original list7
me_list.extend(ls8)
me_list.extend(ls9)
print(me_list)


"""
Python has a set of built-in methods that we can use on lists.
"""
my_list = [1, 2, 3, 3, 9, 5, 3]
list_alpha = ['apple', 'strawberry', 'kiwi', 'orange']
print(my_list, list_alpha)
print(len(my_list), len(list_alpha))
print(max(my_list), max(list_alpha))
list_alpha.extend(my_list)  # The extend() method modifies the original list
print(list_alpha)
my_list.append(10)  # adds an element to the end of the list
print(my_list)
my_list.remove(9)  # removes an item from the list
print(my_list)
print(my_list.count(3))
my_list.insert(2, 8)  # inserts an item at the defined index
print(my_list)
print(my_list[2:5])  # List slicing
print(my_list.pop(4))  # returns and removes an element at the given index
my_list.reverse()  # reverse the order of items in the list
print(my_list)
my_list.sort()  # sort items in a list in ascending order
print(my_list)
dup_list= my_list.copy()  # returns a shallow copy of the list
my_list.sort(reverse=True)
del my_list[2]  # Delete List Elements
print(dup_list)
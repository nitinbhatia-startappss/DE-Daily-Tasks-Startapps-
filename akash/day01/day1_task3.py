#Q check time complexity in set vs list while searching for element
# list example
numbers_list = [10, 20, 30, 40, 50]

# checking element in list
if 30 in numbers_list:
    print("Found in list")
else:
    print("Not found in list")


# set example
numbers_set = {10, 20, 30, 40, 50}

# checking element in set
if 30 in numbers_set:
    print("Found in set")
else:
    print("Not found in set")
    
#time complexity in list is O(n) and in set is O(1) bcz set uses hash lookup    
    

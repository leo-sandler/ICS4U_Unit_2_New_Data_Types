dict1 = {}
dict1[True] = "yes"
print(dict1[True])  # prints "yes"

if True in dict1:  # Use in to sense that something is inside a dictionary
    print("Yes it is")
'''
.clear() - deletes all contents of a dictionary
.items() - returns all key, value pairs
.get(key) - returns the value for the passed key
.keys() - returns a list of all keys, use list()
    ex/ list(dict1.keys())
.values() - returns a list of all values, use list()
    ex/ list(dict1.values())
len() also works with dictionaries
'''
for x in dict1:
    print(x)  # Prints all keys in the dictionary


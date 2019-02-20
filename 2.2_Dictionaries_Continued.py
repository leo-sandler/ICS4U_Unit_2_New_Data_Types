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

# Task 1: Create a dictionary with 4 items and make one value a list. Print out each value of the dictionary using a for
# loop. Also print out each element in the list.


def task_1():
    dict = {"Hello": True, "World": False, "HockeyNumber": 77, "Listing": [1, 2, 3]}
    a = True
    if a == False:
        for x in dict:
            print(dict[x])
            if isinstance(dict[x], list):
                for n in range(len(dict[x])):
                    a = dict[x][n]
                    print(a)
    return dict


# Task 2: Create a function that takes two parameters, one a value and one a dictionary. The function returns the key
# associated with that value.
def task_2(val):
    dictionary = task_1()


# Task 3: Create an example of a list and a dictionary where both would be accessed the same way and return the same
# value.


# Task 4: Create a system that allows the user to type in a word and a definition for multiple words and then print out
# that full dictionary.

# Create a function that takes in a list and converts it to a dictionary where the indices are keys.



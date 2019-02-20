def learning():
    dict1 = {}
    dict1[True] = "yes"
    print(dict1[True])  # prints "yes"
    if True in dict1:  # Use in to sense that something is inside a dictionary
        print("Yes it is")
    for x in dict1:
        print(x)  # Prints all keys in the dictionary
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

# Task 1: Create a dictionary with 4 items and make one value a list. Print out each value of the dictionary using a for
# loop. Also print out each element in the list.


def task_1():
    dictionary = {"Hello": True, "World": False, "HockeyNumber": 77, "Listing": [1, 2, 3]}
    a = True # Change to false when wanting to print. This messes with task 2
    if a is False:
        for x in dictionary:
            print(dictionary[x])
            if isinstance(dictionary[x], list):
                for n in range(len(dictionary[x])):
                    a = dictionary[x][n]
                    print(a)
    return dictionary
task_1()

# Task 2: Create a function that takes two parameters, one a value and one a dictionary. The function returns the key
# associated with that value.

def task_2(val, dictionary):
    return dictionary.get(val)


print(task_2(input("Value: "), task_1()))


# Task 3: Create an example of a list and a dictionary where both would be accessed the same way and return the same
# value.


def task_3():
    dictionary = {0: 1, 1: 2, 2: 3}
    list_ = [1, 2, 3]
    print(dictionary[0])
    print(list_[0])


task_3()


# Task 4: Create a system that allows the user to type in a word and a definition for multiple words and then print out
# that full dictionary.
def task_4():
    dictionary = {}
    for x in range(3):
        key = input("Enter a Word: ")
        definition = input("Define it: ")
        dictionary[key] = definition
    print(dictionary)


task_4()


# Task 5: Create a function that takes in a list and converts it to a dictionary where the indices are keys.
def task_5(listing):
    dictionary = {}
    for x in range(len(listing)):
        dictionary[x] = listing[x]
    print(dictionary)

task_5([5, 4, 3, 2, 1])

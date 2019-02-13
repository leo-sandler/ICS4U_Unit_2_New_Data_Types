car_dictionary = {"year": 2019, "maker": "Honda", "4door": True}
# Made with curly brackets. This is a list that is unordered. Accessed via a square brackets. The key is used
# instead of index values. Keys cannot change, but the key values can.
print(car_dictionary["year"])  # Accessing via the key, year in order to access the key value 2019.
car_dictionary["type"] = "civic type r"  # Adding a type key and also adding "civic type r" to it.
print(car_dictionary["type"])  # Printing civic type r
del car_dictionary["year"]  # Removing the index year and the value 2019 from the dictionary
# print(car_dictionary["year"]) # This will error the code as it has been removed


# TASK 1: Create and print a dictionary (just print(dictionary_name)) that holds proper data for this data type.
hockey_player = {"first_name": "Leo", "last_name": "Sandler", "Position": "Defence", "Number": 77}
print(hockey_player)

# TASK 2: Create a dictionary and delete any key:value pair.
del hockey_player["first_name"]

# TASK 3: Create an empty dictionary and add at least 3 key:value pairs to it.
numbers_empty = {}
numbers_empty["primes"] = 3, 5, 7
numbers_empty["perfect_squares"] = 1, 4, 9
numbers_empty["odd_nums"] = 1, 3, 5

# TASK 4: Create a dictionary and algorithmically delete any key:value pair where the key starts with an “a”.
# (Include some keys that start with “a” , no loop holes plz)
area_codes = {"Toronto": 416, "Atlanta": 404, "Detroit": 313, "Austin": 512}
key_names = []
for x in area_codes:
    if x[0].upper() == "A":
        key_names.append(x)

for x in range(len(key_names)):
    del area_codes[key_names[x - 1]]

print(area_codes)
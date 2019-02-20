# Tuples hold data like a list. They cannot be changed/are immutable.
def learning():
    tuple1 = ("hello", "world")
    tuple2 = "hello", "world"
    if tuple1 == tuple2:
        print("These are equal even if one has brackets and one doesn't.")
    print(tuple1[0])  # Tuples are ordered with index values.
    empty_tuple = ()  # Empty brackets that are round create a tuple.
    print(empty_tuple)
    one_tuple = (3,)  # Tuple with one item.
    print(one_tuple)
    '''# THIS DOESN'T WORK
    tuple_test = "Hello", "World", 
    val = tuple_test[2]
    print(val)
    '''
    ex_tuple = ("t", "h", [3, 4])  # Tuples can hold lists or other mutable things
    # Therefore, the list can be changed within the tuple.
    ex_tuple[2].append(5)
    if 4 in ex_tuple[2]:
        print("It's there")
    print("The tuple lenth is " + str(len(ex_tuple)))
    # REFERENCE TABLE FOR FUNCTIONS WITHIN GOOGLE SLIDES

learning()
# Task 1: Use a series of length 2 tuples to insert points in a 2d list (which would be a representation of the graph)
# and print it as a graph.


def blank_board():
    board_size = 9
    game_board = []
    for b in range(0, board_size):
        game_board.append(["X"] * board_size)
    return game_board


def board_filling(game_board):
    points = [(0, 5), (1, 6), (2, 7), (3, 8)]
    for x in range(len(points)):
        holder = points[x][0]
        holder1 = points[x][1]
        game_board[holder1][holder] = "P"
    return game_board  # Returns upside down. For example, point 1 is 5 down from the top. However, it is 0 across from
    # The first column.


def board_printer():
    final_gb = board_filling(blank_board())
    for r in range(len(final_gb)):
        for c in range(len(final_gb[r])):
            print(final_gb[r][c], end=' ')
        print()
    print("\n")


board_printer()

# Task 2: Create a dictionary of strings and tuples that hold speeds for streets in both km/h and mph and then allow
# it to be searchable via user input.


def speed_kmh_mph():
    street_speeds = {"Yonge": (40, 25), "Autobahn": (130, 81), "Highway 401": (100, 62)}
    unit = input("1) KM/H\n"
                 "2) MPH\n"
                 "Your Input: ")
    street = input("Yonge, Autobahn, or Highway 401\nWhat Street: ")
    print("The speed limit on " + str(street) + " is " + str(street_speeds[street][int(unit) - 1]))


speed_kmh_mph()

# Task 3: Make a function that takes in a dictionary and returns a list of tuples containing each key value pair.


def dictionary_and_lists():
    dictionary = {"Var1": 1, "Var2": 2, "Var3": 3}
    tuples_list = []
    for x in dictionary:
        tuples_list.append((x, dictionary[x]))
    print(tuples_list)


dictionary_and_lists()  # Unsure why there are single quotes around the keys.

"""Restaurant rating lister."""


# put your code here
#Define a function that take in a restaurant file

def restuarant_word_rating (restaurant_file):

# create an empty dictionary
    rest_dictionary = {}
# opens the file
    text_file = open(restaurant_file)
#rstrip each line
    for line in text_file:
        line = line.rstrip()

# split each line at colon
        restaurants_list = line.split(':')
        # print(restaurants_list)
# make each number into an int
        # for restaurant in restaurants_list:
# loop through each list and at index 0, make a key.  Indx 1, make a value
        rest_dictionary[restaurants_list[0]] = restaurants_list[1]

    # print(rest_dictionary)  
    restaurants_in_order = sorted(rest_dictionary)
    # print(restaurants_in_order)
# prints restaurants ratings dictionary
    for restaurant in restaurants_in_order:
        print(f'{restaurant} is rated at {rest_dictionary[restaurant]}.')


restuarant_word_rating("scores.txt")

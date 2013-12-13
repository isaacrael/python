"""Written By: Gil Rael
The following python program demonstrates how to add
key value pairs to a dictionary, print the dictionary,
and determine the length"""

# Initialize Variables

# Define Functions

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']


# Your code here: Add some dish-price pairs to menu!
menu['Lasagna'] = 12.50
menu['Spaghetti'] = 11.50
menu['Tomato Soup'] = 6.50



print "There are " + str(len(menu)) + " items on the menu."
print menu

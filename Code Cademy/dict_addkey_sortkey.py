"""Written By: Gil Rael
The following python program demonstrates how to
add keys to a dictionary, sorting a list under
a certain key in a dictionary, remove an item in
a list, add a number to an integer value associated
with a dictionary"""

# Initialize Variables

# Define Functions

inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 

# Your code here
# Add the pocket key and associated list to inventory dictionary

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sort the items in the list stored under the 'backpack' key

inventory['backpack'].sort()

# Remove dagger from the list of items stored under the backpack key

inventory['backpack'].remove('dagger')

# Add 50 to the number stored under the gold key

inventory['gold'] = 500 + 50

print inventory


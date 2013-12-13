"""Written By: Gil Rael
The following python program demonstrates the use
of the index and insert functions with lists"""

# Initialize Variables

# Define Functions

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

print "The value of duck_index is", duck_index

animals.insert(duck_index,"cobra") # Your code here!

print "\nNote that cobra is now inserted at index 2\n"

print animals # Observe what prints after the insert operation

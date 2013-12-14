"""Written By: Gil Rael
The following python program demonstrates the use
of a for loop in a function that counts the number
of occurrances of a list item"""

# Initialize Variables

# Define Functions

def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    print count
    return count


x = ["fizz","soda","fizz","suds","fizz"]
fizz_count(x)
    


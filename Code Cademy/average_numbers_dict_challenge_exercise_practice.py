"""Written By: Gil Rael
The following python program demonstrates the use
of a function called average that takes a list of numbers
as input and then prints out the average of the numbers.


   Algorithm:

    Step 1:  Create list of numbers called lst = [80,90]
    Step 2:  total_values equals the length of the list
    Step 3:  total_homework equals the sum of the homework scores
    Step 4:  average_homework = float(total_homework / total_values)
    Step 5:  Define function called average 
    
"""

# Initialize Variables

# Define Functions

lst = [80,90]


    
def average(lst):
    for number in (lst):
        total_values = float(len(lst))
        total_homework = float(sum(lst))
        average_homework = float(total_homework / total_values)
    print "Lloyd's average homework score equals", average_homework
    return average_homework
average(lst)

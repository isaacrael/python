"""Written By: Gil Rael
The following python program demonstrates the use
of a function called average that takes a list of numbers
as input and then prints out the average of the numbers.


   Algorithm:

    Step 1:  Create list of numbers called lloyds_homework - lloyds_homework = lloyd['homework']
    Step 2:  total_values equals the length of the list
    Step 3:  total_homework equals the sum of the homework scores
    Step 4:  average_homework = float(total_homework / total_values)
    Step 5:  Define function called average 
    
"""

# Initialize Variables

# Define Functions

lloyd = {
    "name":"Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name":"Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name":"Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


students = [lloyd,alice,tyler]

lloyds_homework = lloyd['homework']

    
def average(lloyds_homework):
    for number in lloyds_homework:
        total_values = len(lloyds_homework)
        total_homework = sum(lloyds_homework)
        average_homework = float(total_homework / total_values)
    print "Lloyd's average homework score equals", average_homework
    return average_homework
average(lloyds_homework)

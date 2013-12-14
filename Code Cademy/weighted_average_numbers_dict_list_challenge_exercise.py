"""Written By: Gil Rael
The following python program demonstrates the use
of a function called get_average that calculates the weighted
average of a student list of homework 10%, quizzes 30%, and tests 60%
and then prints out the weighted average of the numbers.
"""

"""Algorithm:

    Step 1:  Create list students comprised of the dictionaries lloyd, alice, and tyler
             Def the function get_average
             
    Step 2:  total_values equals the length of the list
    Step 3:  total_homework equals the sum of the homework scores
    Step 4:  average_homework = float(total_homework / total_values)
    Step 5:  Define function called get_average
    Step 6:  Repeat steps 2-4 for quizzes & tests 
    
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

print type(lloyd)
    
def get_average(students):
    for item in students:
        total_homework = float(sum(item['homework']))
        print total_homework
        print type(total_homework)
        total_homework_values = len(item['homework'])
        print type(total_homework_values)
        homework_average = float(total_homework / total_homework_values)
        print type(homework_average)
        weighted_homework_average = float((total_homework / total_homework_values) * 0.1)
        print type(weighted_homework_average)
#        print item['name'],"weighted average homework score equals", weighted_homework_average        
        total_quizzes = sum(item['quizzes'])
        print type(total_quizzes)
        total_quiz_values = len(item['quizzes'])
        print type(total_quiz_values)
        quiz_average = float(total_quizzes / total_quiz_values)
        print type(quiz_average)
        weighted_quiz_average = float((total_quizzes / total_quiz_values) * 0.3)
        print type(weighted_quiz_average)
#        print item['name'],"weighted average quiz score equals", weighted_quiz_average        
        total_tests = sum(item['tests'])
        print type(total_tests)
        total_test_values = len(item['tests'])
        print type(total_test_values)
        test_average = float(total_tests / total_test_values)
        print type(test_average)
        weighted_test_average = float((total_tests / total_test_values) * 0.6)
        print type(weighted_test_average)
#        print item['name'],"weighted average test score equals", weighted_test_average
        weighted_average = weighted_homework_average + weighted_quiz_average + weighted_test_average
        print type(weighted_average)
        print item['name'],"weighted average score equals", weighted_average        
get_average(students)

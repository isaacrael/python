"""Written By: Gil Rael
The following python program demonstrates the use
of a function called get_letter_grade to produce a letter
grade for students based on their weighted average score.
"""

"""Algorithm:

    Step 1:  Write a get_letter_grade function that takes score as input and returns a string with the letter grade
     that that student should receive.

These are the grade cutoffs:

Scores 90 or above: return "A"
If 80 <= score < 90: return "B"
If 70 <= score < 80: return "C"
If 60 <= score < 70: return "D"
If score < 60: return "F"

    Step 2:  Pass your function the result of running get_average on lloyd and print the resulting letter grade.


    
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


students = [lloyd]




def get_letter_grade(score):
    if (score >= 90):
        print "Lloyd's grade equals A"
        return "A"
    elif (score >= 80 and score < 90):
        print "Lloyd's grade equals B"
        return "B"
    elif (score >= 70 and score < 80):
        print "Lloyd's grade equals C"
        return "C"
    elif (score >= 60 and score < 70):
        print "Lloyd's grade equals D"
        return "D"
    elif (score < 60):
        print "Lloyd's grade equals F"
        return "F"


    
def get_average(students):
    for item in students:
        total_homework = sum(item['homework'])
        total_homework_values = len(item['homework'])
        homework_average = float(total_homework / total_homework_values)
        weighted_homework_average = float((total_homework / total_homework_values) * 0.1)
#        print item['name'],"weighted average homework score equals", weighted_homework_average        
        total_quizzes = sum(item['quizzes'])
        total_quiz_values = len(item['quizzes'])
        quiz_average = float(total_quizzes / total_quiz_values)
        weighted_quiz_average = float((total_quizzes / total_quiz_values) * 0.3)
#        print item['name'],"weighted average quiz score equals", weighted_quiz_average        
        total_tests = sum(item['tests'])
        total_test_values = len(item['tests'])
        test_average = float(total_tests / total_test_values)
        weighted_test_average = float((total_tests / total_test_values) * 0.6)
#        print item['name'],"weighted average test score equals", weighted_test_average
        weighted_average = weighted_homework_average + weighted_quiz_average + weighted_test_average
        print item['name'],"weighted average score equals", weighted_average
        score = weighted_average
        get_letter_grade(score)
get_average(students)


 

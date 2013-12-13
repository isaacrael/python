"""Written By: Gil Rael
The following python program demonstrates the use
of a function compute_bill to
compute the bill for a shopping list"""

"""Algorithm:  
    Step 1:  Create compute_bill function - Done
    Step 2:  Pass shopping_list, dictionaries stock & prices - Done
    Step 3:  Print shopping_list, stock & prices for testing - Done
    Step 4:  Loop through shopping_list - Done
    Step 5:  Print shopping_list for testing - Done
    Step 6:  Loop through stock - Done
    Step 7:  Print key & values in stock for testing - Done
    Step 8:  Loop through prices - Done
    Step 9:  Print key & values in prices for testing - Done 
    Step 10:  Initialize total = 0 - Done
    Step 11:  Create nested for loops - Done
    Step 12:  If item in shopping list = item in prices then total = total + prices[key] - Done
    Step 13:  Sum total - Done
    Step 14:  Print "Your bill total equals", total - Done

"""

# Initialize Variables

# Define Functions

shopping_list = ["banana","apple","orange"]

food = shopping_list

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}



def compute_bill(food):
    total = 0
    print
    for key in prices:
        for key in stock:
            for item in food:
                if item == key in prices:
                    total = total + prices[key]
        break 
    print "Your bill total equals", total            
compute_bill(food)
    
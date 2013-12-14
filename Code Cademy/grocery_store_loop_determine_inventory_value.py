"""Written By: Gil Rael
The following python program demonstrates the use
of a function to calculate the value of inventory
in a grocery store and print the result"""

"""Algorithm:  
    Step 1:  Create grocery_store_inventory_value function - Done
    Step 2:  Pass dictionaries prices, stock - Done
    Step 3:  Print prices & stock - Done
    Step 4:  Loop through prices - Done
    Step 5:  Print key & values in prices - Done
    Step 6:  Loop through stock - Done
    Step 7:  Print key & values in stock - Done
    Step 8:  Initialize inventory_value = 0 - Done
    Step 9:  Create nested for loops - Done
    Step 10:  Multiply price by stock to get inventory_value = price * stock - Done
    Step 11:  Sum inventory_value - Done
    Step 12:  Print "The value of inventory equals", inventory_value - Done


"""

# Initialize Variables

# Define Functions

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
    
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

def grocery_store_inventory_value(prices,stock):
    print prices
    print stock
    print
    inventory_value = 0
    for key in prices:
        for key in stock:
            print key, "stock : " + str(stock[key])
            print key, "prices : " + str(prices[key])
            inventory_value = inventory_value + (stock[key] * prices[key])   
        break 
    print 
    print "The value of inventory in your grocery store equals", inventory_value            
grocery_store_inventory_value(prices,stock)
    
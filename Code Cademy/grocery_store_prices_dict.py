"""Written By: Gil Rael
The following python program demonstrates the use
of a function grocery_store_inventory and dictionaries
(prices and stock) to print out each item along with it's
associated price & number in stock """

# Initialize Variables



# Define Functions

def grocery_store_inventory(prices,stock):
    for key in prices:
        print key
        print "price : " + str(prices[key])
        print "stock : " + str(stock[key])    
        print
prices = {"banana" : 4,"apple" : 2,"orange" : 1.5,"pear" : 3}
stock = {"banana" : 6,"apple" : 0,"orange" : 32,"pear" : 15}
grocery_store_inventory(prices,stock)

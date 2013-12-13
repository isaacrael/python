"""Written By: Gil Rael the following program
calculates the current amount owed plus interest
after making a payment towards a hotel bill"""

# Initialize variables


# Calculate Hotel bill

def hotel_cost(nights):
    return nights * 140
bill = hotel_cost(5)


# Adds Monthly Interest to New Balance

def add_monthly_interest(balance):
    print "Amount you still owe is", balance * (1 + (0.15 / 12))
    return balance * (1 + (0.15 /12))


# Calculates New Bill after payment has been made

def make_payment(payment, balance):
    balance = balance - payment
    return add_monthly_interest(balance)
new_bill = make_payment(bill/2, bill)


make_payment(100, new_bill)
    
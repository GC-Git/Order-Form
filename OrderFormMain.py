# Program: Lesson 6 Order Form
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Program purpose: The programs purpose is to list total cost of a given number of items.


# Imports
import locale
locale.setlocale(locale.LC_ALL, '')

# Variables
item_price = float(3.5)  # STATIC FOR NOW
item_total = 0
order_total = float(0.0)  # total for the entire order
item_cnt = int(0)  # Item Counter for current item
order_cnt = 0  # Running total for how many boxes for entire order
valid_data = False


# Main Loop Init
cont = ""
while cont.lower() != 'y' and cont.lower() != 'n':
    cont = input('Would you like to place an order? (y/n)')
    username = input("What is your name? ")



## MAIN LOOP ##
while cont.lower() == 'y':

    # valid_data acts as a sentinel for the next sub-loop within the main loop. It must be set to
    # true to go to the next loop
    valid_data = False

    while not valid_data:  # Lists flavors for selection
        print("Please choose one of our flavors. Enter the item number to make a selection.")
        print("Number\tFlavor")
        print("1.\tSavannahs")
        print("2.\tThin Mints")  # Hint: \t in a string is tab
        print("3.\tTag-a-longs")
        print()

        try:
            item = input("Enter item number>")  # Hint: item resolves to a string

        except Exception as inst:  # Grabs all exceptions and prints them
            print("error: ", inst)

        else:  # Runs if the try statement runs without throwing an exception
            if item == '1' or item == '2' or item == '3':  # item must be a string, or converted to a string
                valid_data = True
            else:
                print('\nThat is not an option. I strongly suggest you rethink the'
                      ' choices that have led you to this point in your life.')
                print()

    # Flag reset
    valid_data = False

    while not valid_data:  # Asking the user how many cookies they want within a range in the else statement
        try:
            item_cnt = int(input("How many would you like? "))

        except Exception as inst:
            print("error: ", inst)

        else:
            if 1 <= item_cnt <= 10:  # Users cannot order more than 10 boxes of a single type
                valid_data = True
            else:
                print("Calm down buddy you don't need THAT many cookies.")
    # End of loop

    item_total = item_cnt * item_price  # Calculates total price for current item and amount
    fmt_total = locale.currency(item_total, grouping=True)  # Formats the item total

    # Checks input choice
    if item == '1':
        name = "Savannah"
    elif item == '2':
        name = "Thin Mints"
    else:
        name = "Tag-a-Longs"

    print("Order for {}.".format(username))
    print("Item\tPrice\tQty\tTotal")
    print("\n{}    {}    {}   {}".format(name, item_price, item_cnt, fmt_total))
    print()


    # Flag Reset
    valid_data = False

    ## INPUT CONFIRMATION ##
    while not valid_data:
        try:
            incl = input("Would you like to add this to your order?(y/n) ")
            print()

        except Exception as detail:
            print("Ya goofed: ", detail)

        else:
            if incl.lower() == 'y':
                order_total += item_total
                order_cnt += item_cnt
                valid_data = True
                print("{} was added to your order.".format(name))
            elif incl.lower() == 'n':
                print("{} was not added to your total.".format(name))
                valid_data = True
            else:
                print("What? WHAT? I CANT UNDERSTAND YOU!")
            print()
    ## END INPUT CONFIRMATION ##

    try:
        cont = ""
        while cont.lower() != 'y' and cont.lower() != 'n':
            cont = input("Would you like to add another order?(y/n) ")
    except Exception as detail:
        print("error: ", detail)

## END MAIN LOOP ##

## FINAL SALE DISPLAY ##
fmt_total = locale.currency(order_total, grouping=True)
print("You have ordered {} items costing {}".format(order_cnt, fmt_total))
print("Thank you for using this program {}.".format(username))
## END FINAL SALE DISPLAY ##

# Program: Lesson 3a Order Form
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Program purpose: The programs purpose is to list total cost of a given number of items. Each items with different costs and quantity.


#Variable Definitions
import locale
locale.setlocale ( locale.LC_ALL, '')
username = 'Meatbag'
item_cnt = int(0)                                       #Item Counter
order_total = float(0.0)                                #total for the order
item_price = float(3.5)
valid_data = False
item_total = 0
#End of variable definitions

username = input("What is your name? ")

cont = "" 
while cont.lower() != 'y' and cont.lower() != 'n':
    cont = input('Would you like to place an order? (y/n)') #Sentinal

while cont.lower() == 'y':
    valid_data = False
    
    while not valid_data:
        # Cookie list #
        print("Please choose one of our flavors. Enter the item number to make a selection.")
        print("Number\tFlavor")
        print("1.\tSavannahs")
        print("2.\tThin Mints")
        print("3.\tTag-a-longs")
        print() #blank line
        item = input("Enter item number>") #Entering as string
        #End of Cookie List#

        if item == '1' or item == '2' or item == '3':
            valid_data = True
        else:
            print("\nThat is not an option. I strongly suggest you rethink the choices that have led you to this point in your life.")

    valid_data = False

    while not valid_data:
        item_cnt = int(input("How many would you like? "))

        if 1 <= item_cnt <= 10:
            valid_data = True
        else:
            print("Calm down buddy you dont need THAT many cookies.")

    item_total = item_cnt * item_price
    fmt_total = locale.currency(item_total, grouping = True)

    # Determine cookie name for output
    if item == 1:
        name = "Savannah"
    elif item == 2:
        name = "Thin Mints"
    else:
        name = "Tag-a-Longs"

    print("Order for {}.".format(username))
    print("Item\tPrice\tQty\tTotal")
    print("\n{}    {}    {}   {}".format(name,item_price,item_cnt,fmt_total))
    print() # blank line
    
    valid_data = False

    while not valid_data:
        incl = input("Would you like to add this to your order?(y/n)")
        print()
        if incl.lower() == 'y':
            order_total = order_total + item_total
            item_cnt = item_cnt + 1
            valid_data = True
            print("{} was added to your order.".format(name))
        elif incl.lower() == 'n':
            print("{} was not added to your total.".format(name))
            valid_data == True
        else:
            print("what? WHAT? I CANT UNDERSTAND YOU!")
        print()
    cont = input("Would you like to add another order?")
#End main loop

fmt_total = locale.currency(item_total, grouping = True)
print("You have ordered {} items costing {}".format(item_cnt,fmt_total))
print("Thank you for using this program. Press any key to exit.")

# Program: Lesson 3a Order Form
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Program purpose: The programs purpose is to list total cost of a given number of items. Each items with different costs and quantity.

#Variable Definitions
cont = input('Would you like to place an order? (y/n)') #Sentinal
item_cnt = int(0)                                       #Item Counter
order_total = float(0.0)                                #total for the order
#End of variable definitions

print("Order for Gordon Clark")
print("Item   Price   Qty   Total")

while cont.lower() == 'y':
    #User input 
    item_name = input("Item name? ")
    item_qty = int(input("How many of these items are you purchasing? "))
    item_price = float(input("How much does this item cost per unit? "))
    #End user input
    item_total = item_qty * item_price
    order_total = order_total + item_total
    item_cnt = item_cnt + item_qty

    print("{}    {}    {}   ${}".format(item_name,item_price,item_qty,item_total))
    cont = input("Would you like order another item?(y/n)")

print("You have ordered {} items costing ${}".format(item_cnt,order_total))
print("Thank you for using this program. Press any key to exit.")

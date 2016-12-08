# Program: Lesson 6 Order Form
# Programmer: Gordon Clark
# Date: Dec 1, 2016
# Program purpose: Display an order for girl scout cookies, inputted by the user.


import os  # Used in cls() for clearing the screen

# *****
#   Classes
# *****

class OrderForm(object):
    """
    Takes a two dimensional list formatted as [[Name, Price] [Name, Price]] to use as a list of available items. The
    blank_lines_before_input is how many blank lines will be displayed after the menu's but before the input is
    requested. ||IMPORTANT||: The last parameter is the two dimensional list previously mentioned.
    -----------------------------------------------------------

    == CLASS VARIABLES ==
    display_dict                - This is the options available to the user and what will be returned when menu input
                                is requested.
    == ATTRIBUTES ==
    items_available             - a 2D list passed in on class creation containing items available to order.
    menu_choice                 - This variable is used for user input throughout the class.
    blank_lines_before_input    - Sets the number of lines after the menu but before the input line. max of 20,
                                default: 2.
    user_cart                   - The users cart formatted as [[Name,Price,Quantity],[Name,Price,Quantity]]
    build_item                  - The item to be built [Name, Price, Quantity] before being added to the users cart.
    order_total                 - The total cost of the current order
    """
    # TODO Exception handling if something other than a 2d list is passed to the class.

    disp_dict = {
        "a": "[a]dd",
        "d": "[d]elete",
        "q": "[q]uit"
    }

    def __init__(self, blank_lines_before_input, items_available):
        """
        Class Initialization
        :param blank_lines_before_input: How many blank lines get printed before asking for input
        :param items_available: a 2D list of available items formatted as ["Name", int(price)]
        """

        self.__items_available = items_available
        self.__menu_choice = None
        self.__blank_lines_before_input = blank_lines_before_input
        self.__user_cart = []
        self.__build_item = []
        self.__order_total = 0

    def disp_blank_lines(self, lines="default"):
        """
        Prints blank lines.
        :param lines: default=2, takes an integer from 0-20
        """
        if lines == "default":
            lines = self.__blank_lines_before_input
        if 0 < lines <= 20:  # sets the max loop number to 20, so 20 blank lines after
            for i in range(0, lines):  # loops the number of times set in the parameter
                print("")

    def disp_items_available(self,get_input=False, clear=False):
        """
        Displays items available for purchase. If get_input is set to True the user will be asked which item they want
        to purchase, the quantity, and then confirm the purchase; at which point it will be added to the users cart.

        :param get_input: if True the user will select an item+quantity for purchase, which will then be added to the
        cart
        :param clear: if True the screen will be cleared before displaying
        :return:
        """
        if clear:
            self.cls()

        print("Available Items:")
        index = 0  # The below loop lists out the items in items_available
        for item in self.__items_available:
            index += 1
            print("{}. {}  ${}".format(index, item[0], item[1]))

        if get_input:  # TODO Turn this into a more generic method that can add to other lists in the class.
            """
            |||| ADD ITEM INPUT ||||
            If get_input is set to true the following code will execute.
            This consists of two while loops and a for loop.
            """
            self.disp_blank_lines()
            """
            The First while loop gets the users input, converts it to an integer, and clones the corresponding item
            from items_available into build_item. build_item acts as a temporary container while the user selects the
            item they want and the quantity. Keep in mind build_item must be a |||COPY||| of the item from
            items_available. If you just set it to equal what you want, it ends up pointing at the same place in memory
            and modifies the items_available variable instead of creating a new item. Took me like an hour of debugging
            to figure that one out.
            """
            while True:
                try:
                    self.__menu_choice = int(input("Choose item for purchase>"))
                    if self.__menu_choice in range(1, len(self.__items_available)+1):
                        self.__build_item = list(self.__items_available[self.__menu_choice - 1])
                        break
                except Exception:
                    print("Enter a valid number.")

            """
            The seconds while loop asks the user how many items they want (while allowing them to cancel the order).
            It then appends it onto build_item, completing the list of name, quantity, and price.
            """
            while True:  # Asks how many and adds it to the build_item
                try:
                    self.__menu_choice = int(input("How many would you like to purchase? (0 = Cancel) >"))
                    if self.__menu_choice == 0:
                        return
                    elif 0 < self.__menu_choice < 200:
                        self.__build_item.append(self.__menu_choice)
                        break
                except Exception:
                    print("Enter a valid number.")

            """
            The final process. This searches the user_cart to see if the user has already purchased an item with the
            same name ( user_cart[0] ). If it finds a match, it adds the quantity from build_item to the quantity of the
            already present item. If no match is found, it appends build_item onto user_cart.
            """
            found_match = False
            for index, item in enumerate(self.__user_cart, start=0):
                if self.__build_item[0] == item[0]:  # If names match b/w build item and list at all
                    self.__user_cart[index][2] += self.__build_item[2]
                    found_match = True
            if found_match == False:
                self.__user_cart.append(self.__build_item)

    def disp_menu(self, get_input=False, clear=False):
        """
        Displays the menu. If get_input is set to True the method will return the item chosen

        :param get_input:
        :param clear: if True the screen will be cleared before displaying
        :return: if get_input is a true a selection will be returned (via input) from the menu_choice list
        """
        if clear:
            self.cls()

        print("Menu:")
        for key in self.disp_dict:  # Prints the menu
            print(self.disp_dict[key], end="\n")

        if get_input:
            self.disp_blank_lines()
            while True:
                self.__menu_choice = input(">")
                if self.__menu_choice in self.disp_dict:
                    break
            return self.__menu_choice

    def cls(self):  # Clears the console
        """
        Clears the screen. May not work properly in all consoles.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def disp_cart(self, clear=False):
        """
        Displays user_cart to the screen in an ordered format along with the totals at the bottom.

        :param clear: if True the screen will be cleared before displaying
        """
        if clear:
            self.cls()

        if len(self.__user_cart) > 0:
            print("{:=^30}{}{:=^30}".format("", "CURRENT ORDER", ""))
            print("{:15}{:15}{:15}{:15}".format("Item #", "Name", "Price Per.", "Count"))
            print("{:-^60}".format(""))
            for index in range(len(self.__user_cart)):  # Prints a row
                print(str(index + 1), end=".")
                print("{:.<13}{:.<15}{:.<15}{:.<15}".format(
                                                            self.__user_cart[index][0],
                                                            "",
                                                            self.__user_cart[index][1],
                                                            self.__user_cart[index][2]))

            self.__order_total = 0
            for i in self.__user_cart:
                self.__order_total += i[2]*i[1]
            print("")
            print("{:.<15}{:.<15}{:.<15}{:.<15}".format("Totals:", ".", self.__order_total, ""))

    def delete_item(self):
        """
        Requests input and removes the item chosen from the user_cart.
        """
        while True:
            try:
                self.__menu_choice = int(input("Which item would you like to delete? (0 = Cancel) >"))
                if self.__menu_choice == 0:
                    break
                elif 0 < self.__menu_choice < len(self.__user_cart)+1:
                    self.__user_cart.pop(self.__menu_choice-1)
                    break
            except Exception as e:
                print(e)
                print("Please enter a valid choice.")


# **********
#   Main Program
# **********
"""
scoutcookies is the 2 dimensional list that will be passed into OrderForm during instantiation. It will act as the list
of items 'stocked' in the 'shop' with an associated price for each item.
"""
scoutcookies = [
    ["Savannah", 3.5],
    ["Thin Mints", 3.5],
    ["Tag-a-longs", 3.5],
    ["Peanut Butter", 3.5],
    ["Sandwich", 3.5]
]
order = OrderForm(2, scoutcookies) # Class is instantiated here, passing the 2d list in


# ====
# Main Loop
# ====
while True:
    order.cls()
    print(r"""
  ___ __ ____ __      ____  ___ __  _  _ ____     ___ __   __ __ _ __ ____ ____
 / __|  |  _ (  )    / ___)/ __)  \/ )( (_  _)   / __)  \ /  (  / |  |  __) ___)
( (_ \)( )   / (_/\  \___ ( (_(  O ) \/ ( )(    ( (_(  O |  O )  ( )( ) _)\___ \
 \___(__|__\_)____/  (____/\___)__/\____/(__)    \___)__/ \__(__\_|__|____|____/

    """)

    order.disp_cart()
    user_choice = order.disp_menu(get_input=True)

    if user_choice == "a":  # Add
        order.disp_items_available(get_input=True, clear=True)
    elif user_choice == "d":  # Delete
        order.delete_item()
    elif user_choice == "q":  # Quit
        exit()



var_1 = 5

try:
    var_2 = int(input("input>"))
    average = var_1 / var_2
    print(average)

    # If you print the instance of Exception, itll display the error.
    # Its a shortcut so you don't have to make a code for everything.
    # Works well for development, but not releases
except Exception as detail:
    print("error: ", detail)

else:
    print(var_2)
finally:
    print("unconditional print out")

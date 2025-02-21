# If else notes

# Different types: str, int, float
        # str: This textual things and it is denoted with "" or ''
        # int: These are whole numbers. Can be negative, but they 0, 1, 2, 3, etc. NO DECIMALS
        # float: These are decimal numbers. Can be 1.0, 2.0, but they can also be 1.3, and 2.6

def check_if_num_is_pos():

    # gather input from user of any number.
    # note: this number may include decimals (float)

    # when creating a variable:
        # 1. we are declaring the variable name
        # 2. put =
        # 3. put what you are going to store in that variable
    
    # input returns a variable of type str
    paul: float = float(input("Enter a number"))

    if paul > 0:
        print("The number is positive.")
    elif paul < 0:
        print("The number is negative.")
    else:
        # else is default
        print("The number is zero")    \
        
def grade_checker():
    # ask the user for a number btwn 0-100. Whole numbers only.
    # Then we want to check to see if they passed or failed (passing is anything above a 60)
    # Then make sure to check that they entered a number btwn 0-100
    pass
if __name__ == "__main__":
    check_if_num_is_pos()

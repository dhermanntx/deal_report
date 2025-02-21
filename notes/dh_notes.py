# If else notes

# Different types: str, int, float
        # str: This is Textual things denoted with "" or ''
        # int: These are whole numbers. Can be negative but they are 0, 1, 2, 3 etc. NO DECIMALS
        # float: These are decimal numbers. Can be 1.0, 2.0 can also be 1.3 and 2.6

def check_if_num_is_pos():

    # gater input from user of any number.
    # note this number may include decimals. (float)

    # when creating a variable:
        # 1. we are declaring the variable name.
        # 2. put = signs
        # 3. put what you going to store in that variable
        
    # input returns a variable of type str
    number: float = float (input("Enter a number"))

    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative.")
    else:
        # else is default
        print("The number is zero")


def grade_checker():
    # ask the user for a number between 0-100. Whole numbers only.
    # Then we want to check to see if they passed or failed (passing is anything above a 60)
    # Then make sure to check that they entered a number between 0-100.

    # define what a grade is. Gather Grade.
    grade: int = int (input("What is your grade?"))

    # run our if statements

    if grade < 59:
        print("You failed!")
    elif grade >= 60 and grade < 100:
        print("You Passed!")
    else:
        print("Invalid Entry")
    

if __name__ == "__main__":
    grade_checker()
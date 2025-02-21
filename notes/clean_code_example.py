# the program will ask a user for a number, first it will check to see if it is positive or not
# then it will check the grade of the user to see if they passed or failed
# finally it will check to see if the grade is even or odd


# these functions are like building blocks to a puzzle. They perform certain and specific actions, unique to themselves.
def check_if_pos(grade: int):
    if grade > 0:
        print("positive")
    elif grade < 0:
        print("negative")
    else:
        print("number is zero")

def grade_checker(grade: int):
    if grade >= 60 and grade < 100:
        print("passed")
    elif grade > 0 and grade < 60:
        print("failed")
    else:
        print("invalid number entered")

def even_or_odd(grade: int):
    if grade % 2 == 0 or grade == 0:
        print("the number is even")
    else:
        print("the number is odd")

def super_grade_checker():
    # ask for the number
    grade: int = int(input("What was your grade: "))
    return grade

if __name__ == "__main__":
    grade_input: int = super_grade_checker()
    check_if_pos(grade_input)
    grade_checker(grade_input)
    even_or_odd(grade_input)
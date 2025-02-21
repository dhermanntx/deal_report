# the program will ask a user for a number, first it will check to see if it is positive or not
# then it will check the grade of the user to see if they passed or failed
# finally it will check to see if the grade is even or odd

def super_grade_checker():
    # ask for the number
    grade: int = int(input("What was your grade: "))
    
    if grade > 0:
        print("positive")
    elif grade < 0:
        print("negative")
    else:
        print("number is zero")

    if grade >= 60 and grade < 100:
        print("passed")
    elif grade > 0 and grade < 60:
        print("failed")
    else:
        print("invalid number entered")

    if grade % 2 == 0 or grade == 0:
        print("the number is even")
    else:
        print("the number is odd")

if __name__ == "__main__":
    super_grade_checker();
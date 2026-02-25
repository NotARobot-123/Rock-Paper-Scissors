# Functions go here

def yes_no(question):
    while True:

        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please select yes or no")


def instructions():
    """prints instructions"""
    print("""
    ******* instructions *******
    
        roll the dice to win
         """)


# Main Routine
want_instructions = yes_no("Do you want the instructions?")

if want_instructions == "yes":
    instructions()

print()
print("program continues")

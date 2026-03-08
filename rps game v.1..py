#Name: String Checker
#By: Grayden Farrer
#This code will check that the outputs from the string match the expected output.


#Check that users have entered a valid option based on list
def string_checker(question, valid_ans=("yes","no")):


    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is a word on the list
            if item == user_response:
                return item

            #checks if the user response is the same as
            #the first letter of an item in the list
            elif user_response == item[0]:
                return item

        #print error if user does not enter valid answer
        print(error)
        print()

#Displays instructions
def instructions():
    """prints instructions"""
    print("""
    ******* instructions *******

        To begin, choose the number of rounds. 
        Then, play against the computer.
        you must pick R for rock, P for paper or S for scissors.
        The rules are as follows, paper beats rock, rock beats scissors. scissors beats paper.
         """)

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if (to_check) == "":
            return "infinite"

        try:
            response = int(to_check)

            #checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("Welcome to RPS Game")
print()

#ask user if they want instructions
want_instructions = string_checker("Do you want the instructions?")

if want_instructions == "yes":
    instructions()



# ask user for number of rounds
num_rounds = int_check("How many rounds would you like? push <enter> for infinite mode   ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#game loop starts here
while rounds_played < num_rounds:

    #rounds headings
    if mode == "infinite":
        rounds_heading = f"\n()()() Round {rounds_played + 1} (infinite mode) ()()()"
    else:
        rounds_heading = f"\n [][][] Round {rounds_played + 1} of {num_rounds} [][][]"

    print(rounds_heading)
    print()

    #get user choic
    user_choice = string_checker("choose: ", rps_list)
    print("you chose: ", user_choice)

    # if user choice is exit code, break
    if user_choice == "xxx":
       break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / stats area
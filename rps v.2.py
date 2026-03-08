#Name: String Checker
#By: Grayden Farrer
#This code will check that the outputs from the string match the expected output.
import random

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

#asks for amp=ount of rounds
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

#compares user and computer choice and gives win / lose / tie
def rps_compare(user, comp):

    if user == comp:
        round_result = "tie"

    # there are 3 ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"


    # if it's not a win / tie then it's a loss
    else:
        round_result = "lose"

    return round_result

# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

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

    #randomly chooses from rps for computer
    comp_choice = random.choice(rps_list[:-1])

    result = rps_compare(user_choice, comp_choice)

   # adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = " Its a tie!"
    elif result == "lose":
        rounds_lost += 1
        feedback = " you lose!"
    else:
        feedback = " you win!"

    #set up round feedback and output it user
    # add it to game history list
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    # game loop ends here

    # game history / stats area

if rounds_played > 0:
    #claculate statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # output game stats
    print(" game statistics")
    print(f"won: {percent_won:.2f} \t "
          f"lost: {percent_lost:.2f} \t "
          f"tied: {percent_tied:.2f}")

    # ask user if they want to see game history
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("thanks for playing")

else:
    print("oops you chickened out")
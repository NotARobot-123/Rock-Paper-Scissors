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


def instructions():
    """prints instructions"""
    print("""
    ******* instructions *******

        To begin, choose the number of rounds. 
        Then, play against the computer.
        you must pick R for rock, P for paper or S for scissors.
        The rules are as follows, paper beats rock, rock beats scissors. scissors beats paper.
         """)



# main routine starts here
print()
print("Rock, Paper Scissors!!")
print()

#ask user if they want instructions
want_instructions = string_checker("Do you want the instructions?")

if want_instructions == "yes":
    instructions()


#Name: String Checker
#By: Grayden Farrer
#This code will check that the outputs from the string match the expected output.


#Check that users have entered a valid option based on list
def string_checker(question, valid_ans):

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


# Main routine goes here

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions?",
                                   yes_no)
if "yes":
    print("you chose yes")

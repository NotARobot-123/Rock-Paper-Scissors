
#Check that users have entered a valid option based on list
def string_checker(user_response, valid_ans):
    while True:
        for item in valid_ans:
            #check if the user response is a word on the list
            if item == user_response:
                return item

            #checks if the user response is the same as
            #the first letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"


#Automated testing is below in the form (test_case, expected_value)



#run tests
for item in to_test:
    #Retrievetest case and expected value
    case = item [0]
    expected = item[1]

    # get actual value
    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    #compare actual and expected and output pass / fail
    if actual == expected:
        print(f"  !!! Passed Case: {case}, expected: {expected}, received: {actual} !!!")
    else:
        print(f"  *** Failed Case: {case}, expected: {expected}, received: {actual} ***")






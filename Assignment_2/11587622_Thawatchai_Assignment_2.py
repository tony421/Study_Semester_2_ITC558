# ITC558 - Programming Principles
# Assignment 2
# Thawatchai Jidsodsai (11587622)

# This program is developed for Dr Ho Coaching Centre
# to calculate a tuition fee of each courses of its students.

# constant list value of available programming languages
PG_LANG = ['python', 'java', 'c++']

# constant dictionary value of standard lesson price of each programming languages
PRICE_STD = {'python': 300, 'java': 200, 'c++': 175}

# constant dictionary value of additional hour price of each programming languages
PRICE_ADD_HR = {'python': 200, 'java': 150, 'c++': 175}

# constant dictionary value of test price of each programming languages
PRICE_TEST = {'python': 250, 'java': 150, 'c++': 170}

# constant dictionary value of minimum hours of standard lesson of each programming languages
MIN_STD = {'python': 5, 'java': 4, 'c++': 6}

# constant value of minimum hours of additional hour of each programming languages
MIN_ADD_HR = {'python': 5, 'java': 10, 'c++': 7}

# constant value of minimum hours of test of each programming languages
MIN_TEST = {'python': 5, 'java': 2, 'c++': 2}

print("----------------------------------------------------------------------------------------------")
print("Welcome to Dr Ho Coaching Centre")
print("----------------------------------------------------------------------------------------------")

# initialise 'cmd_repeat' = 'y' for executing the first loop of the program
# and 'cmd_repeat' will be the command for continuing the program
cmd_repeat = 'y'
while(cmd_repeat == 'Y' or cmd_repeat == 'y'): # if 'cmd_repeat' is 'Y' or 'y' then continue the program
    print("")

    # initialise 'lang' = '' for executing the first loop of entering a programming language
    # and 'lang' will be used to store the entered language
    # and will be used for the key of a language's price and minimum hours
    lang = ""

    # use 'not in' operator to check that
    # if entered value is not in the list of programming language, then enter a value again
    while (lang not in PG_LANG):
        # use lower() function of string to lower the case so that used to match the value in the list
        lang = input("Enter the name of the programming language: ").lower()

    # initialise 'num_std' = '-1' for executing the first loop of entering the number of lessons
    num_std = -1

    # if entered numbers of lessons are less than minimum numbers of lesson of the entered language
    #   , then enter a value again
    # use 'lang' as the key to find minimum numbers of lesson of entered language in dictionary
    while (num_std < MIN_STD[lang]):
        num_std = int(input("Enter the number of lessons: "))

    # initialise 'num_add_hr' = '-1' for executing the first loop of entering the additional hours
    num_add_hr = -1

    # if entered additional hours are less than minimum numbers of additional hours of the entered language
    #   , then enter a value again
    # use 'lang' as the key to find minimum numbers of additional hours of entered language in dictionary
    while (num_add_hr < MIN_ADD_HR[lang]):
        num_add_hr = int(input("Enter the additional hours: "))

    # initialise 'num_test' = '-1' for executing the first loop of entering the number of test
    num_test = -1

    # if entered numbers of test are less than minimum numbers of test of the entered language
    #   , then enter a value again
    # use 'lang' as the key to find minimum numbers of test of entered language in dictionary
    while (num_test < MIN_TEST[lang]):
        num_test = int(input("Enter the number of test: "))

    print("")

    fee_std = num_std * PRICE_STD[lang] # calculate the fee of standard lessons
    print("Tuition fee for the lessons (in dollars): ", fee_std)

    fee_add_hr = num_add_hr * PRICE_ADD_HR[lang] # calculate the fee of additional hours
    print("Tuition fee for additional hours (in dollars): ", fee_add_hr)

    fee_test = num_test * PRICE_TEST[lang] # calculate the fee of tests
    print("Tuition fee for the tests (in dollars):", fee_test)

    print("")
    print("Total tuition fee (in dollars): ", sum([fee_std, fee_add_hr, fee_test])) # calculate the total fee

    print("")
    # ask users for continuing the program
    cmd_repeat = input("Do you want to compute the tuition fee for another student? ")

print("", "Good bye.", sep="\n")


# ITC558 - Programming Principles
# Assignment 2
# Thawatchai Jidsodsai (11587622)

#
#

PG_LANG = ['python', 'java', 'c++']
PRICE_STD = {'python': 300, 'java': 200, 'c++': 175}
PRICE_ADD_HR = {'python': 200, 'java': 150, 'c++': 175}
PRICE_TEST = {'python': 250, 'java': 150, 'c++': 170}
MIN_STD = {'python': 5, 'java': 4, 'c++': 6}
MIN_ADD_HR = {'python': 5, 'java': 10, 'c++': 7}
MIN_TEST = {'python': 5, 'java': 2, 'c++': 2}

print("----------------------------------------------------------------------------------------------")
print("Welcome to Dr Ho Coaching Centre")
print("----------------------------------------------------------------------------------------------")

cmd_repeat = 'y'
while(cmd_repeat == 'Y' or cmd_repeat == 'y'):
    print("")

    lang = ""
    while (lang not in PG_LANG):
        lang = input("Enter the name of the programming language: ").lower()

    num_std = -1
    while (num_std < MIN_STD[lang]):
        num_std = int(input("Enter the number of lessons: "))

    num_add_hr = -1
    while (num_add_hr < MIN_ADD_HR[lang]):
        num_add_hr = int(input("Enter the additional hours: "))

    num_test = -1
    while (num_test < MIN_TEST[lang]):
        num_test = int(input("Enter the number of test: "))

    print("")

    fee_std = num_std * PRICE_STD[lang]
    print("Tuition fee for the lessons (in dollars): ", fee_std)

    fee_add_hr = num_add_hr * PRICE_ADD_HR[lang]
    print("Tuition fee for additional hours (in dollars): ", fee_add_hr)

    fee_test = num_test * PRICE_TEST[lang]
    print("Tuition fee for the tests (in dollars):", fee_test)

    print("")
    print("Total tuition fee (in dollars): ", sum([fee_std, fee_add_hr, fee_test]))

    print("")
    cmd_repeat = input("Do you want to compute the tuition fee for another student? ")

print("", "Good bye.", sep="\n")


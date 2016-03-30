# ITC558 - Programming Principles
# Assignment 2
# Thawatchai Jidsodsai (11587622)

#
#

PG_LANG = ['Python', 'Java', 'C++']
PRICE_STD = {'Python': 300, 'Java': 200, 'C++': 175}
PRICE_ADD_HR = {'Python': 200, 'Java': 150, 'C++': 175}
PRICE_TEST = {'Python': 250, 'Java': 150, 'C++': 170}
MIN_STD = {'Python': 5, 'Java': 4, 'C++': 6}
MIN_ADD_HR = {'Python': 5, 'Java': 10, 'C++': 7}
MIN_TEST = {'Python': 5, 'Java': 2, 'C++': 2}

print("----------------------------------------------------------------------------------------------")
print("Welcome to Dr Ho Coaching Centre")
print("----------------------------------------------------------------------------------------------")

cmd_repeat = 'Y'
while(cmd_repeat == 'Y' or cmd_repeat == 'y'):
    print("")

    lang = ""
    while (lang not in PG_LANG):
        lang = input("Enter the name of the programming language: ")

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


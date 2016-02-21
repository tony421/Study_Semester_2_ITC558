import math

PRICE_GA_TICKET = 90
PRICE_RGS_TICKET = 150
PRICE_P_TICKET = 250
PRICE_LP_TICKET = 350
is_input_invalid = False


def calculateSaleAmount(ticket_price, ticket_number):
    ticket_number_int = parseInt(ticket_number)
    if type(ticket_number_int) == int:
        return ticket_number_int * ticket_price
    else:
        global is_input_invalid
        is_input_invalid = True
        return "The input is invalid!!!"


def parseInt(val):
    try:
        tempFloat = float(val)
        if tempFloat % math.floor(tempFloat) == 0:
            return int(tempFloat)
        else:
            return False
    except ValueError:
        return False

print("----------------------------------------------------------------------------------------------")
print("Mount Everest Motor Racing Circuit (MEMRC)")
print("----------------------------------------------------------------------------------------------")

num_ga_ticket = input("Please enter the number of tickets sold for General Admission: ")
num_rgs_ticket = input("Please enter the number of tickets sold for Reserved Grandstand Seating: ")
num_p_ticket = input("Please enter the number of tickets sold for The Precinct: ")
num_lp_ticket = input("Please enter the number of tickets sold for Lunch Packages on Everest: ")

print("", "Thank You!", "", sep="\n")

sale_amount_ga = calculateSaleAmount(PRICE_GA_TICKET, num_ga_ticket)
print("The sale amount of tickets for General Admission (in dollars):", sale_amount_ga)

sale_amount_rgs = calculateSaleAmount(PRICE_RGS_TICKET, num_rgs_ticket)
print("The sale amount of tickets for Reserved Grandstand Seating (in dollars): ", sale_amount_rgs)

sale_amount_p = calculateSaleAmount(PRICE_P_TICKET, num_p_ticket)
print("The sale amount of tickets for The Precinct (in dollars): ", sale_amount_p)

sale_amount_lp = calculateSaleAmount(PRICE_LP_TICKET, num_lp_ticket)
print("The sale amount of tickets for Lunch Packages on Everest (in dollars): ", sale_amount_lp)

if is_input_invalid is False:
    print("", "The total sale amount: " + str(sum([sale_amount_ga, sale_amount_rgs, sale_amount_p, sale_amount_lp])), "", sep="\n")
else:
    print("", "The total sale amount: the total can not be calculated because of the invalid inputs!", "", sep="\n")

print("Good Bye.")
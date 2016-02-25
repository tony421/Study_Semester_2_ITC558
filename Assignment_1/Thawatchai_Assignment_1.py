import math # import math for using "floor" function

PRICE_GA_TICKET = 90 # constant value of price for General Admission ticket
PRICE_RGS_TICKET = 150 # constant value of price for Reserved Grandstand Seating ticket
PRICE_P_TICKET = 250 # constant value of price for The Precinct ticket
PRICE_LP_TICKET = 350 # constant value of price for Lunch Packages on Everest ticket
is_input_invalid = False # True = there is some invalid inputs, False = there is no invalid inputs


# function used for calculate sale amount of ticket
def calculateSaleAmount(ticket_price, sold_ticket_number):
    sold_ticket_number_int = parseInt(sold_ticket_number) # convert string of sold ticket to integer
    if type(sold_ticket_number_int) == int:
        # if number of sold ticket is integer then multiply it by the price and return
        return sold_ticket_number_int * ticket_price
    else:
        # if it is not integer
        global is_input_invalid # declare for using global variable
        is_input_invalid = True # set to True because there is some invalid input
        return "The input is invalid!!!" # return error message


# function used for converting string to integer
def parseInt(val):
    try:
        tempFloat = float(val) # convert string to float
        if tempFloat % math.floor(tempFloat) == 0: # if the argument likes "1.0" or "21.0"
            return int(tempFloat) # then convert float to integer and return
        else:
            return False
    except ValueError: # this exception occurs when the argument can not be converted to float or int
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
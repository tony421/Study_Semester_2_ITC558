import math

# function for converting string to integer
def parseInt(val):
    try:
        tempFloat = float(val) # convert string to float

        # if the number is zero
        if tempFloat == 0:
            # then return zero
            return 0
        else:
            modDivisor = math.floor(tempFloat) # find the input without decimal
            if modDivisor > 0:
                # if the divisor for modulus is more than zero (this condition used to avoid the error "Modulus by zero)
                # the condition also means that the input is not between 0.1 and 0.9
                # then check that the number is integer or not
                if tempFloat % modDivisor == 0: # if the argument is integer likes "1.0" or "21.0"
                    return int(tempFloat) # then convert float to integer and return
                else:
                    return False
            else:
                return False
    except ValueError: # this exception occurs when the argument cannot be converted to float or int
        return False
##
# @file our_library.py
# @author Alena Klimecká
# @date 27.4.2020
# @brief math library of the calculator
#



##
# @brief Addition ( num1 + num2 )
#
# @param num1 First number to be added (augend)
# @param num2 Second number to be added (addend)
# @return Returns the sum of two numbers
#
def our_add(num1: float, num2: float) -> float:
    return num1 + num2



##
# @brief Subtraction ( num1 - num2 )
#
# @param num1 First number of a subtraction (minuend)
# @param num2 Second number of a subtraction (subtrahend)
# @return Returns the difference of two numbers
def our_sub(num1: float, num2: float) -> float:
    return num1 - num2



##
# @brief Multiplication ( num1 * num2 )
#
# @param num1 First number to by multiplied (multiplicand)
# @param num2 Second number to by multiplied (multiplier)
# @return Returns the product of two numbers
#
def our_mul(num1: float, num2: float) -> float:
    return num1 * num2


##
# @brief Division ( num1 / num2 )
#
# @param num1 First number of a division (dividend)
# @param num2 Second number of a division (divisor)
# @exception "NaN" if divisor happens to be zero
# @return Returns the quotient of two numbers
#
def our_div(num1: float, num2: float) -> float:
    if num2 == 0:                                # cannot be divided by zero
        return float('NaN')
    return num1 / num2


##
# @brief Factorial of the number ( num! )
#
# @param num The number of which factorial will be calculated
# @exception "NaN" if the number is negative
# @return Returns the factorial of the number
#
def our_fact(num: int) -> float:                # factorial can only be called with a positive integer
    if num < 0:
        return float('NaN')
    factorial: int = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

##
# @brief Raising to a power ( num^exp )
#
# @param num Base of a power
# @param exp Exponent of a power
# @exception "NaN" if base is zero and exponent negative at once
# @return Returns the value of a power
#
def our_pow(num: float, exp: float) -> float:
    if (num == 0) & (exp < 0):
        return float('NaN')                         # cannot call with num1 == 0 & exp < 0
    return num ** exp


##
# @brief Extraction of a root ( num1√num2 )
#
# @param num1 Index (degree) of the root
# @param num2 Radicand
# @exception "NaN" if degree of the root is equal to zero, or if it is negative and radicand is zero
# @return Returns the value of the root
#
def our_sqrt(num1: float, num2: float) -> float:
    if num1 == 0:                                   # cannot call with num1 == 0
        return float('NaN')
    if (num1 < 0) & (num2 == 0):                    # cannot call with num1 < 0 num2 == 0
        return float('NaN')
    root = our_pow(num2, 1/num1)
    return root


##
# @brief Absolute value ( |num| )
#
# @param num The number of which the absolute value will be calculated
# @return Returns the absolute value of the number
#
def our_abs(num: float) -> float:
    if num >= 0:
        return num
    if num < 0:
        return -num

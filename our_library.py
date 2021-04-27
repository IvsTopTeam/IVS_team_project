# the function gets two parameters and returns num1 + num2
def our_add(num1: float, num2: float) -> float:
    return num1 + num2


# the function gets two parameters and returns num1 - num2
def our_sub(num1: float, num2: float) -> float:
    return num1 - num2


# the function gets two parameters and returns num1 * num2
def our_mul(num1: float, num2: float) -> float:
    return num1 * num2


# the function gets two parameters and returns num1 / num2
def our_div(num1: float, num2: float) -> float:
    if num2 == 0:                                # cannot be divided by zero
        return float('NaN')
    return num1 / num2


# the function gets one parameter and return its factorial
def our_fact(num: int) -> float:                # factorial can only be called with a positive integer
    if num < 0:
        return float('NaN')
    factorial: int = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


# the function gets two parameters and returns num^(exp)
def our_pow(num: float, exp: float) -> float:
    if (num == 0) & (exp < 0):
        return float('NaN')
    return num ** exp


# the function gets two parameters and returns num1√(num2)
def our_sqrt(num1: float, num2: float) -> float:     # cannot call with num1 == 0
    if num1 == 0:
        return float('NaN')
    if (num1 < 0) & (num2 == 0):
        return float('NaN')
    root = our_pow(num2, 1/num1)
    return root


# the function gets a number and returns its absolute value
def our_abs(num: float) -> float:
    if num >= 0:
        return num
    if num < 0:
        return -num

#
def our_add(num1: float, num2: float) -> float:
    return num1 + num2


def our_sub(num1: float, num2: float) -> float:
    return num1 - num2


def our_mul(num1: float, num2: float) -> float:
    return num1 * num2


def our_div(num1: float, num2: float) -> float:
    return num1 / num2


def our_fact(num: int) -> float:    # faktorial lze zavolat pouze s celym cislem!
    if num < 0:
        raise Exception
    factorial: int = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


def our_pow(num: float, exp: float) -> float:
    return num ** exp


def our_sqrt(num1: float, num2: float) -> float:
    sqrt: float = num2
    for i in range(0, 100):
        sqrt = ((num1 - 1) * sqrt / num1) + (num2 / (num1 * our_pow(sqrt, (num1 - 1))))
    return sqrt


def our_abs(num: float) -> float:
    if num >= 0:
        return num
    if num < 0:
        return -num

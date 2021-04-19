from decimal import *


def our_add(num1: float, num2: float) -> float:
    return num1 + num2


def our_sub(num1: float, num2: float) -> float:
    return num1 - num2


def our_mul(num1: float, num2: float) -> float:
    return num1 * num2


def our_div(num1: float, num2: float) -> float:
    return num1 / num2


def our_fact(num: int) -> float:    # faktorial lze zavolat pouze s celym cislem
    if num < 0:
        raise Exception
    factorial: int = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


def our_pow(num: float, exp: float) -> float:
    return num ** exp


def our_sqrt(num1: float, num2: float) -> float:     # nelze zavolat s num1 == 0
    if num1 == 0:
        raise Exception
    root = our_pow(num2, 1/num1)
    return root


def our_abs(num: float) -> float:
    if num >= 0:
        return num
    if num < 0:
        return -num

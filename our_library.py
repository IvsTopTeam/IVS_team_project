def our_add(num1, num2):
    return num1 + num2


def our_sub(num1, num2):
    return num1 - num2


def our_mul(num1, num2):
    return num1 * num2


def our_div(num1, num2):
    return num1 / num2


def our_fact(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


def our_pow(num, exp):
    return num ** exp


def our_sqrt(num1, num2):
    sqrt = num2
    for i in range(0, 100):
        sqrt = ((num1 - 1) * sqrt / num1) + (num2 / (num1 * our_pow(sqrt, (num1 - 1))))
    return 0


def our_abs(num):
    if num > 0:
        return num
    if num < 0:
        return -num

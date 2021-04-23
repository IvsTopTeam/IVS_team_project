# funkce dostane dva parametry a vraci jejich soucet
def our_add(num1: float, num2: float) -> float:
    return num1 + num2


# funkce dostane dva parametry a vraci jejich rozdil
def our_sub(num1: float, num2: float) -> float:
    return num1 - num2


# funkce dostane dva parametry a vraci jejich soucin
def our_mul(num1: float, num2: float) -> float:
    return num1 * num2


# funkce dostane dva parametry a vraci jejich podil
def our_div(num1: float, num2: float) -> float:
    return num1 / num2


# funkce dostane jeden parametr a vraci jeho faktorial
def our_fact(num: int) -> float:    # faktorial lze zavolat pouze s celym cislem
    if num < 0:
        raise Exception
    factorial: int = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


# funkce dostane dva parametry, vraci mocninu num^(exp)
def our_pow(num: float, exp: float) -> float:
    return num ** exp


# funkce dostane dva parametry, vraci jejich num1√(num2)
def our_sqrt(num1: float, num2: float) -> float:     # nelze zavolat s num1 == 0
    if num1 == 0:
        raise Exception
    root = our_pow(num2, 1/num1)
    return root


# funkce dostane cislo a vraci jeho absolutni hodnotu
def our_abs(num: float) -> float:
    if num >= 0:
        return num
    if num < 0:
        return -num

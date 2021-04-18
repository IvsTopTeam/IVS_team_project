import our_library as lib


def eval(float_result, string_main, operation):
    result = 0
    if operation == "+":
        result = lib.our_add(float_result, float(string_main))
    elif operation == "-":
        result = lib.our_sub(float_result, float(string_main))
    elif operation == "×":
        result = lib.our_mul(float_result, float(string_main))
    elif operation == "÷":
        result = lib.our_div(float_result, float(string_main))
    elif operation == "√":
        result = lib.our_sqrt(float_result, float(string_main))
    elif operation == "ⁿ":
        result = lib.our_pow(float_result, float(string_main))
    return result


def clicked_number(string, number):
    if string == "0" and number == ".":
        string = "0."
    elif string != "0" and number == ".":
        if "." not in string and len(string) < 10:
            string = string + number
    elif string == "0" and number == "0":
        string = "0"
    elif string == "0" and number != "0":
        string = number
    elif string != "0" and len(string) < 10:
        string = string + number
    elif string != "0" and len(string) >= 10:
        string = string

    return string


def clicked_delete(string):
    if string == "0":
        string = "0"
    else:
        string = string[:-1]
    if len(string) == 0:
        string = "0"
    return string


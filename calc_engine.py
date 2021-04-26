import our_library as lib

display_limit = 10
dec_round = 2


def display_num(float_result):
    num_str = "0"
    num_str = str(round(float_result, dec_round))
    # if the result is xx.0, it removes the .0 part
    if round(float_result, dec_round).is_integer():
        num_str = num_str[:-2]  # removes .0

    # if the number is too long to display it displays too long error
    if len(num_str) > display_limit:
        num_str = "Too large!"

    return num_str


def result_overflow(result_string):
    if len(result_string) > display_limit:
        print("len")
        print(len(result_string))
        return True
    return False


def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def evaluation(float_result, string_main, operation):
    result = 0
    if not isfloat(string_main):
        string_main = "0"

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
    if not isfloat(string):
        string = "0"

    if string == "0" and number == ".":
        string = "0."
    elif string != "0" and number == ".":
        if "." not in string and len(string) < display_limit:
            string = string + number
    elif string == "0" and number == "0":
        string = "0"
    elif string == "0" and number != "0":
        string = number
    elif string != "0" and len(string) < display_limit:
        string = string + number
    elif string != "0" and len(string) >= display_limit:
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


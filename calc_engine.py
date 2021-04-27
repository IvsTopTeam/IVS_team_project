##
# @file calc_engine.py
# @author David Novak
# @date 27.4. 2020
# @brief Module with functions, which are used in GUI class methods to do the calculator job
#

import our_library as lib
display_limit = 10      # implementation limit of number digits on display
dec_round = 2           # implementation limit of number of decimal digits to round to


##
# @brief                This function provides proper displaying of numbers
# @param float_result   float number to display
# @return num_str       string with number to display
#
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


##
# @brief            This function find out if the string on input can be converted to float
# @param string     string to find out
# @return           boolean value, true if in string can be converted to float, false of not
#
def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


##
# @brief                This function evaluates operation using our_library functions
# @param float_result   first operand
# @param string_main    second operand
# @param operation      operation to do with two operands
# @return error         error message if there some error occured, or "ok" if ok
# @return result        result of the operation
#
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
        if float(string_main) == 0:     # division by 0 error
            return "Math Error", result
        result = lib.our_div(float_result, float(string_main))
    elif operation == "√":
        if float_result == 0:     # zero root error
            return "Math Error", result
        result = lib.our_sqrt(float_result, float(string_main))
    elif operation == "ⁿ":
        try:
            result = lib.our_pow(float_result, float(string_main))
        except OverflowError:
            return "Too large!", result
    return "ok", result


##
# @brief            This function adds new digit to string with number
# @param string     string with current number
# @param digit      digit to add
# @return           string with added digit
#
def clicked_number(string, digit):
    if not isfloat(string) and string != "-":
        string = "0"

    if string == "0" and digit == ".":
        string = "0."
    elif string != "0" and digit == ".":
        if "." not in string and len(string) < display_limit:
            string = string + digit
    elif string == "0" and digit == "0":
        string = "0"
    elif string == "0" and digit != "0":
        string = number
    elif string != "0" and len(string) < display_limit:
        string = string + digit
    elif string != "0" and len(string) >= display_limit:
        string = string

    return string


##
# @brief            This function deletes last character from input string
# @param string     input string
# @return           string with deleted last character
#
def clicked_delete(string):
    if string == "0":
        string = "0"
    else:
        string = string[:-1]
    if len(string) == 0:
        string = "0"
    return string


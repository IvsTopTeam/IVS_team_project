import calc_gui as g


def clicked_number(number):
    if g.operation == "none": # first operator section
        if g.num1 == "0" and number == ".":
            g.num1 = "0."
        elif g.num1 == "0" and number == "0":
            g.num1 = "0"
        elif g.num1 == "0" and number != "0":
            g.num1 = number
        elif g.num1 != "0" and len(g.num1) < 10:
            g.num1 = g.num1 + number
        elif g.num1 != "0" and len(g.num1) >= 10:
            g.num1 = g.num1
    else: # second operator section
        if g.num2 == " " and number == ".":
            g.num2 = "0."
        elif  g.num2 == " " and number == "0":
            g.num2 = "0"
        elif g.num2 == " " and number != "0":
            g.num2 = number
        elif g.num2 != " " and len(g.num2) < 10:
            g.num2 = g.num2 + number
        elif g.num2 != " " and len(g.num2) >= 10:
            g.num2 = g.num2

    print(g.num1 + " " + g.operation + " " + g.num2)


def clicked_delete():
    if g.num1 == "0":
        g.num1 = g.num2
    elif g.operation == "none":
        g.num1 = g.num1[:-1]
    elif g.operation != "none" and g.num2 == " ":
        g.operator = "none"
    elif g.operation != "none" and g.num2 != " ":
        g.num2 = g.num2[:-1]

    print(g.num1 + " " + g.operator + " " + g.num2)

def clicked_operation(operation):






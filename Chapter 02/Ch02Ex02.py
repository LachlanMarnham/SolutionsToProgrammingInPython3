import cmath
import math
import sys


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x


# Fix formatting of numbers like (-1-2j)-->-(1+2j) and (-1+2j)-->-(1-2j)
def fix_complex_sign(number):
    if number.real < 0:
        if number.imag < 0:
            new_number = complex(abs(number.real), abs(number.imag))
            changed_flag = True
        else:
            new_number = complex(abs(number.real), -abs(number.imag))
            changed_flag = True
    else:
        new_number = number
        changed_flag = True
    if abs(new_number.real) < sys.float_info.epsilon:
        new_number = complex(abs(new_number.real), new_number.imag)
    return new_number, changed_flag


def make_equation(a, b, c, x_1, x_2):
    a_template = "{a}x\N{SUPERSCRIPT TWO}"
    b_template = "{sign_b} {b}x"
    c_template = "{sign_c} {c}"
    template = a_template
    if abs(b) >= sys.float_info.epsilon:
        template += b_template
    if abs(c) >= sys.float_info.epsilon:
        template += c_template
    template += " = 0"

    sign_x_1 = ''
    sign_x_2 = ''
    sign_b = ' +'
    sign_c = ' +'
    if type(x_1) == complex:
        x_1, sign_changed_1 = fix_complex_sign(x_1)
        if sign_changed_1:
            sign_x_1 = '-'
    if type(x_2) == complex:
        x_2, sign_changed_2 = fix_complex_sign(x_2)
        if sign_changed_2:
            sign_x_2 = '-'
    if b < 0:
        sign_b = ''
    if c < 0:
        sign_c = ''
    equation = (template + " \N{RIGHTWARDS ARROW} "
                           "x = {sign_x_1}{x1}").format(**locals())
    if x_2 is not None:
        equation += " or x = {sign_x_2}{x2}".format(**locals())
    return equation


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x_1 = None
x_2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x_1 = -(b / (2 * a))
    if abs(x_1) < sys.float_info.epsilon:
        x_1 = 0.0
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x_1 = (-b + root) / (2 * a)
    x_2 = (-b - root) / (2 * a)

print(make_equation(a, b, c, x_1, x_2))

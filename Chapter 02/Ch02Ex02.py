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
            print(err.__str__())
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


def make_equation(coef_a, coef_b, coef_c, solution_1, solution_2):
    a_template = "{a}x\N{SUPERSCRIPT TWO}"
    b_template = "{sign_b} {b}x"
    c_template = "{sign_c} {c}"
    template = a_template

    # Linear and constant terms will only appear in the equation if their
    # coefficients are non-zero
    if abs(coef_b) >= sys.float_info.epsilon:
        template += b_template
    if abs(coef_c) >= sys.float_info.epsilon:
        template += c_template
    template += " = 0"

    # Handle negative numbers with the replacement, e.g., '+-6'-->'-6'
    sign_x_1 = ''
    sign_x_2 = ''
    sign_b = ' +'
    sign_c = ' +'
    if type(solution_1) == complex:
        solution_1, sign_changed_1 = fix_complex_sign(solution_1)
        if sign_changed_1:
            sign_x_1 = '-'
    if type(solution_2) == complex:
        solution_2, sign_changed_2 = fix_complex_sign(solution_2)
        if sign_changed_2:
            sign_x_2 = '-'
    if coef_b < 0:
        sign_b = ''
    if coef_c < 0:
        sign_c = ''
    equation = (template + " \N{RIGHTWARDS ARROW} "
                           "x = {sign_x_1}{x1}").format(**locals())
    if solution_2 is not None:
        equation += " or x = {sign_x_2}{x2}".format(**locals())

    return equation


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

# x_1 and x_2 are the roots of the equation
x_1 = None
x_2 = None
discriminant = (b ** 2) - (4 * a * c)
# If the discriminant is zero, there is only one root
if abs(discriminant) <= sys.float_info.epsilon:
    x_1 = - (b / (2 * a))
    if abs(x_1) < sys.float_info.epsilon:
        x_1 = 0.0
else:
    # If the discriminant is positive, there are two real roots
    if discriminant > 0:
        delta = math.sqrt(discriminant)
    # If the discriminant is negative, there are two complex roots
    else:
        delta = cmath.sqrt(discriminant)

    x_1 = (-b + delta) / (2 * a)
    x_2 = (-b - delta) / (2 * a)

print(make_equation(a, b, c, x_1, x_2))

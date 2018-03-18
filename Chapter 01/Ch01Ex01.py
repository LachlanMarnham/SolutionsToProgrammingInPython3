import sys

# Initialise the digits 0-9, and store them in a list called digits
ZERO = ['  ***  ', ' *   * ', '*     *', '*     *', '*     *', ' *   * ',
        '  ***  ']
ONE = [' * ', '** ', ' * ', ' * ', ' * ', ' * ', '***']
TWO = [' *** ', '*   *', '*  * ', '  *  ', ' *   ', '*    ', '*****']
THREE = [' *** ', '*   *', '    *', '  ** ', '    *', '*   *', ' *** ']
FOUR = ['   *  ', '  **  ', ' * *  ', '*  *  ', '******', '   *  ', '   *  ']
FIVE = ['*****', '*    ', '*    ', '**** ', '    *', '*   *', ' *** ']
SIX = [' *** ', '*    ', '*    ', '**** ', '*   *', '*   *', ' *** ']
SEVEN = ['*****', '    *', '   * ', '  *  ', ' *   ', '*    ', '*    ']
EIGHT = [' *** ', '*   *', '*   *', ' *** ', '*   *', '*   *', ' *** ']
NINE = [' ****', '*   *', '*   *', ' ****', '    *', '    *', '    *']

digits = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

try:
    # Read in the argument from the command line, store as a string
    number_string = sys.argv[1]

    row = 0
    while row < 7:
        line = ''
        for digit in number_string:
            dig_int = int(digit)
            # a = digits[dig_int] locates the right number in the list
            # digits. b = a[row] locates the right row of a.
            # b.replace('*', digit) replaces each astrix in b with the number
            # corresponding to digit. digits[dig_int][row].replace('*', digit)
            # does this all in one step.
            line += digits[dig_int][row].replace('*', digit) + '  '
        print(line)
        row += 1

# Don't raise if the user forgets to enter an argument at the command line
except IndexError:
    print("Error, try: python Ch01Ex01.py <integer>.")

# Don't raise if the argument entered at the command line is not an int
except ValueError:
    print("Error: argument must be an int.")

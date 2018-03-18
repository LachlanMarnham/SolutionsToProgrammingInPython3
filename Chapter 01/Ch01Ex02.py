# initialise relevant variables
numbers = []
count = 0
total = 0
lowest = None
highest = None
TEMPLATE = 'count = {0} sum = {1} lowest = {2} highest = {3} mean = {4}'

# while loop will continue to seek new inputs until the user enters Enter, at
# which point loop terminates
while True:
    new_input = input('enter a number or Enter to finish: ')
    if new_input != '':
        # attempt to convert user input to a number. If input is not
        # convertible to a number, catch the exception and warn the user
        try:
            new_number = float(new_input)
        except ValueError:
            print('invalid input!')
        numbers.append(new_number)
        count += 1
        total += new_number
        if lowest is None:
            lowest = new_number
            highest = new_number
        elif new_number < lowest:
            lowest = new_number
        elif new_number > highest:
            highest = new_number
    else:
        break

# calculate the mean of the numbers and print results
try:
    mean = total / count
    print('numbers: ', numbers)
    print(TEMPLATE.format(count, total, lowest, highest, mean))
except ZeroDivisionError:
    print('no numbers were entered')

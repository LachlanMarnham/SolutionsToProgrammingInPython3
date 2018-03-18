from math import floor


def find_average(number_list, with_extras=False):
    running_sum = 0
    for number in number_list:
        running_sum += number
    number_count = len(number_list)
    average = running_sum / number_count
    # with_extras is an optional flag which will return only average if set
    # to False (which it is by default) and will also return the sum and
    # sample size of the numbers if set to True
    if with_extras:
        return average, running_sum, number_count
    else:
        return average


def bubble_sort(number_list):
    swapped_flag = True
    while swapped_flag:
        n = 0
        swapped_flag = False
        for i in range(len(number_list) - 1 - n):
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
                swapped_flag = True
        n += 1


def find_median(my_list):
    bubble_sort(my_list)
    max_index = len(my_list) - 1
    # If my_list contains an even number of elements, find the average of the
    # two center-most elements. Otherwise, return the centre-most element
    if len(my_list) % 2 == 0:
        i = floor((max_index / 2))
        # The with_extras flag takes its default value (False) here
        return find_average(my_list[i:i+2])
    else:
        median_index = max_index // 2
        return my_list[median_index]


# initialise relevant objects
numbers = []
count = 0
total = 0
lowest = None
highest = None
TEMPLATE = 'count = {0} sum = {1} lowest = {2} highest = {3} ' \
           'mean = {4} median = {5}'

# while loop will continue to seek new inputs until the user enters Enter,
# at which point loop terminates
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
    mean, total, count = find_average(numbers[:], with_extras=True)
    median = find_median(numbers[:])
    print('numbers: ', numbers)
    print(TEMPLATE.format(count, total, lowest, highest, mean, median))
except ZeroDivisionError:
    print('no numbers were entered')


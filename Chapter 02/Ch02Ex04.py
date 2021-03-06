import sys
from xml.sax.saxutils import escape

USAGE_TEXT = """
usage:
python3 Ch02Ex04.py [maxwidth=int] [format=str] <infile.csv> <outfile.html>

maxwidth is an optional integer; if specified, it sets the maximum
number of characters that can be output for string fields,
otherwise a default of 100 characters is used.

format is the format to use for numbers; if not specified it 
defaults to ".0f". For allowed format types, see Figure 2.6.
"""
NUMBER_TEMPLATE = "<td align='right'>{0:{1}}</td>\n"


def main():
    # Get parameters from command line
    max_width, int_format = process_options(sys.argv)
    if max_width is None or int_format is None:
        return
    input_filename = sys.argv[-2]
    output_filename = sys.argv[-1]
    table = ""
    table += print_start()
    count = 0

    # Read in data from file, instead of with call to input()
    file_object = open(input_filename, "r")
    data = file_object.read()
    file_object.close()

    # Convert data to html
    lines = data.splitlines()
    for line in lines:
        try:
            if count == 0:
                color = "lightgreen"
            elif count % 2 == 0:
                color = "white"
            else:
                color = "lightyellow"
            table = print_line(table, line, color, max_width, int_format)
            count += 1
        except EOFError:
            break
    table += print_end()

    # Dump html into output file
    output_file_object = open(output_filename, "w")
    output_file_object.write(table)
    output_file_object.close()


def process_options(cmd_args):
    # Set the defaults. These will change if the user has defined alternatives
    max_width = 100
    int_format = '.0f'
    # Produce the USAGE_TEXT if user asks for help, otherwise handle maxwidth
    # and format if they are defined by the user
    if cmd_args[1] in ('-h', '--help'):
        print(USAGE_TEXT)
        return None, None
    else:
        # cmd_args[1:-2] excludes the script name, input filename and output
        # filename, leaving only maxwidth and format should they exist.
        for arg in cmd_args[1:-2]:
            if 'maxwidth' in arg:
                width_num = arg.replace('maxwidth=', '')
                try:
                    # If the user enters maxwidth=5.0, this is a valid integer
                    # but not a valid int. We should handle this.
                    if '.' in width_num:
                        max_width = int(float(width_num))
                    else:
                        max_width = int(width_num)
                # If the user entered a width that couldn't be converted to an
                # int terminate the program
                except ValueError:
                    print('Incorrect value for '
                          'maxwidth. Enter an '
                          'integer.')
                    max_width = None
                    break
            elif 'format' in arg:
                int_format = arg.replace('format=', '')
                # Call str.format(...) and terminate the program if an
                # exception is raised
                try:
                    '{0:{1}}'.format(1, int_format)
                except ValueError as e:
                    print('Incorrect value for format. '
                          + e.__str__() + '.')
                    int_format = None
                    break

        return max_width, int_format


def print_start():
    return "<table border='1'>\n"


def print_end():
    return "</table>\n"


def print_line(table, line, color, max_width, int_format):
    table += "<tr bgcolor='{0}'>\n".format(color)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            table += "<td></td>\n"
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                # const NUMBER_TEMPLATE is defined so this line isn't too long
                table += NUMBER_TEMPLATE.format(round(x), int_format)
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= max_width:
                    field = escape(field)
                else:
                    field = "{0} ...".format(escape(field[:max_width]))
                table += "<td>{0}</td>\n".format(field)
    table += "</tr>\n"
    return table


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:           # start of quoted string
                quote = c
            elif quote == c:            # end of quoted string
                quote = None
            else:
                field += c              # other quote inside quoted string
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c                  # accumulating a field
    if field:
        fields.append(field)            # adding the last field
    return fields


main()

import sys
from xml.sax.saxutils import escape


def main():
    # Get files from command line.
    # Usage: python3 Ch02Ex03.py <input_filename> <output_filename>
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    max_width = 100
    table = ""
    table += print_start()
    count = 0

    # Read in data from file instead, instead of with call to input()
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
            table = print_line(table, line, color, max_width)
            count += 1
        except EOFError:
            break
    table += print_end()

    # Dump html into output file
    output_file_object = open(output_filename, "w")
    output_file_object.write(table)
    output_file_object.close()


def print_start():
    return "<table border='1'>\n"


def print_end():
    return "</table>\n"


def print_line(table, line, color, max_width):
    table += "<tr bgcolor='{0}'>\n".format(color)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            table += "<td></td>\n"
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                table += "<td align='right'>{0:d}</td>\n".format(round(x))
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

import sys
import unicodedata


def print_unicode_table(word_list):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)  # Stop at surrogate pairs

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        for word in word_list:
            if word is None or word in name.lower():
                continue
            else:
                break
        else:
            print("{0:7}  {0:5X}  {0:3c}  {1}".format(
                    code, name.title()))
        code += 1


words = [None]
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string_1] [string_2] ...".format(sys.argv[0]))
        words = []
    else:
        words = [word.lower() for word in sys.argv[1:]]

if words:
    print_unicode_table(words)

import string
import sys

from collections import defaultdict


words = defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1

for word, count in sorted(words.items(), key=lambda w: w[1]):  # Sort by count
    print("'{0}' occurs {1} times.".format(word, count))

"""
There are three files to test on in ./data
Usage: python Ch03Ex02.py data/file1.txt data/file2.txt data/file3.txt
"""

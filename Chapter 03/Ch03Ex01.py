from collections import defaultdict
from string import punctuation
import sys

# sites will insert an empty set when we try to call sites[k]
# when k not in sites
sites = defaultdict(set) 

for file_name in sys.argv[1:]:
    for line in open(file_name):
        i = 0
        while True:
            site = None
            i = line.find("http://", i)
            if i > -1:
                i += len("http://")
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        i = j
                        break
                if site and "." in site:
                    sites[site.rstrip(punctuation)].add(file_name)
            else:
                break

print(sites)

"""
There are three files to test on in ./data
Usage: python Ch03Ex01.py data/file1.txt data/file2.txt data/file3.txt
"""

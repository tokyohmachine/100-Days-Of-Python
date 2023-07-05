#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
#and summing up the integers.

import re         #imports the regular expression library

hand = open("regex_sum_1505244.txt", "r")
numlist = []

for line in hand:
    line = line.rstrip()
    integers = re.findall('([0-9]+)', line)

    for number in integers:
        numlist.append(int(number))

print(sum(numlist))
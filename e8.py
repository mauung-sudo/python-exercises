words = []
result = []

import itertools
from itertools import chain

with open("e8.txt") as file:
    for line in file:

        #lines.append(line.split())
        #words = list(itertools.chain.from_iterable(lines))
        words = line.strip().split()

        for element in words:
            if element not in result:
                result.append(element)
                result.sort()

print(result)








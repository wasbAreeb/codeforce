
# 26 January 2026

# Brute force. It was more mathemcatical. I need to focus on combinatorics, geometry and number theory.

import math

t = int(input().strip())

result = []
for i in range(t):
    n = int(input().strip())

    if n % 2 != 0:
        result.append(0)
    else:
        result.append(math.floor((n/4)+1))

for i in result:
    print(i)




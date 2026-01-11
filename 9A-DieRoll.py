
# Date : 07/1/2026. Successfully solved by own

# from fractions import Fraction

# y, w = map(int, input().split())

# maxs = y if y > w else w

# events = 6
# sample = 0
# for i in range(maxs, events+1):
#     sample += 1


# if sample/events:
#     if sample/events == 1:
#         print("1/1")
#     else:
#         print(Fraction(sample, events))

# elif sample == 0:
#     print("0/1")

# The Above solutions has the time complexity of O(n). However it can be reduced to constant TC.

from fractions import Fraction

y, w = map(int,input().split())

max_event = max(y,w)

sample = 7 - max_event

if (sample/6) == 1:
    print("1/1")
elif sample == 0:
    print("0/1")
else:
    print(Fraction(sample, 6))

# This solutions has less code, better optimized, clearn and constant TC
#!/usr/bin/python3
import math
n = 24
sat = 0
sun = 1
# Your code should be below this line
if n < 1 or n > 31:

    print("Not valid")

elif ((n - 1) % 7) == sat or ((n - 1) % 7) == sun:
    print("Weekend")

else:
    print("Weekday")
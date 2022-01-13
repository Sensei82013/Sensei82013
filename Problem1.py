#!/usr/bin/python3
import math as m
n = 100

# Your code should be below this line
if n > 0 and n % 2 == 0 and (m.sqrt(5*(n**2) + 4)%2==0 or m.sqrt(5*(n**2) - 4) % 2 == 0 or m.sqrt(5*(n**2) + 4)%3==0 or m.sqrt(5*(n**2) - 4) % 3 == 0):

    print("Yes")
else:
    print("No")

#If your input is number = 2 or 34 or 144, the output should be "Yes".
#If your input if number = 4 or 1 or 5 or -8, the output should be "No". Note that 1 and 5 in this example are part of the 

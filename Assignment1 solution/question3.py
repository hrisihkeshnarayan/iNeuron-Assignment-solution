##3. Write a Python program to find the volume of a sphere with diameter 12 cm.
## Formula: V=4/3 * π * r 3

import math
D = int(input("Enter Diameter of sphere :"))
r=D/2
V=4/3 * math.pi * (r**3)
print(V)

## output :
##Enter Diameter of sphere :12
##904.7786842338603

## QUESTION

## 2. Implement List comprehensions to produce the following lists.
## Write List comprehensions to produce the following Lists
## A = ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
## B = ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
## C = ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
## D = [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
## E = [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
## F = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

## SOLUTION 

## CODE(A)

[x for x in "ACADGILD"]

## OUTPUT

['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

## CODE(B)

[x*i for i  in range(1,4) for x in 'XYZ']

## OUTPUT

['X', 'Y', 'Z', 'XX', 'YY', 'ZZ', 'XXX', 'YYY', 'ZZZ']

## CODE(C)

[x*i  for x in 'XYZ' for i  in range(1,4)]

## OUTPUT

['X', 'XX', 'XXX', 'Y', 'YY', 'YYY', 'Z', 'ZZ', 'ZZZ']

## CODE(D)

[[x+y] for y in range(0,3) for x in range(2,5)]

## OUTPUT

[[2], [3], [4], [3], [4], [5], [4], [5], [6]]

## CODE(E)

[[x,x+1,x+2,x+3] for x in range(2,6)]

## OUTPUT

[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

## CODE(F)

[(y,x) for x in range(1,4) for y in range(1,4)]

## OUTPUT

[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]





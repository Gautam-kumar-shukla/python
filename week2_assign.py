
# Q1 A +ve integer m is sum of squares if it can be written as K + L
# where K >0 and L > 0 and both K and L are perfect square.

# First find K and L for any given number

from math import *


def isperfectsquare(n):
     x = int(sqrt(n))
     if n == x*x:
        return True
     else:
         return False


def find_k_l(m):
    i = 0
    found = False
    for i in range(1, m//2 + 1):
        if isperfectsquare(i) and isperfectsquare(m-i):
            found = True
            break

    if found:
        return i, m-i
    else:
        return False


# print("k and l for 30 is ", find_k_l(30))

# Q2 A string with parenthese is well brackted if all parenthese are well matching
# Every opening bracket has matching closing bracket


def wellmatching(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count = count + 1
        elif s[i] == ')':
            count = count - 1;

    if count == 0:
        return True
    else :
        return False

str = "(22)"
#print("is well matching :", wellmatching(str))



# Q3. A list rotation consists of taking the last element and moving it to the front. For instance,
# if we rotate the list [1,2,3,4,5], we get [5,1,2,3,4]. If we rotate it again, we get [4,5,1,2,3].

# Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns
# the list l after k rotations. If k is not positive, your function should return l unchanged.
# Note that your function should not change l itself, and should return the rotated list.


def rotatelist(l, k):
    rotlist = l[:]
    for i in range(k):
        rotlist = [rotlist[-1]] + rotlist[:-1]
    return rotlist

l = [1, 2, 3, 4, 5, 6, 7, 8]
k = 9
print("rotatelist", rotatelist(l, k))





# "Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal."
# Link to the question - https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr) # it is taking length of array and storing in n
    a = 0 # Positive elements in array
    b = 0 # Negative elements
    c = 0 # number of zeros
    
    for x in arr: # to check all elements one by one and sort them 
        if x > 0:
             a += 1
        elif x < 0:
            b += 1
        else:
            c += 1
            
    a = a/n # calculating ratio 
    b = b/n
    c = c/n
    
    print(f"{a:.6f}") #print ratio in 6 decimal points
    print(f"{b:.6f}")
    print(f"{c:.6f}")
            
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


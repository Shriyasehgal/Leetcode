#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0
    while(len(ar)!=0):
        for j in range (1,n):
            if (ar[0]==ar[j]):
                count=count+1
                ar.remove(ar[0])
                ar.remove(ar[j])
                n=n-2
                break
            
            else:
                ar.remove(ar[0])
                n=n-1
        
    
            


    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)


#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/bin/python3  

import math  
import os  
import sys  

#  
# Complete the 'extraLongFactorials' function below.  
#  
# The function accepts INTEGER n as parameter.  
#  

def extraLongFactorials(n):  
    # Initialize result to 1  
    result = 1  
    # Calculate factorial by iterating from 1 to n  
    for i in range(1, n + 1):  
        result *= i  
    # Print the result as we need to output it  
    print(result)  

if __name__ == '__main__':  
    n = int(input().strip())  
    extraLongFactorials(n)


# 

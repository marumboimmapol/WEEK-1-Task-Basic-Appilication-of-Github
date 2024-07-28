#!/usr/bin/env python
# coding: utf-8

# In[11]:


def virusIndices(p, v):  
    n = len(p)  
    m = len(v)  
    matches = []  

    # Loop through each possible starting point in p  
    for i in range(n - m + 1):  
        mismatch_count = 0  
        
        # Compare the substring of p with v  
        for j in range(m):  
            if p[i + j] != v[j]:  
                mismatch_count += 1  
            
            # If we have more than 1 mismatch, stop checking this substring  
            if mismatch_count > 1:  
                break  
        
        # If we have 0 or 1 mismatches, record the starting index  
        if mismatch_count <= 1:  
            matches.append(i)  

    # Print results  
    if matches:  
        print(" ".join(map(str, matches)))  
    else:  
        print("No Match!")  

if __name__ == '__main__':  
    t = int(input().strip())  # Read the number of test cases  
    for _ in range(t):  
        first_multiple_input = input().rstrip().split()  
        p = first_multiple_input[0]  
        v = first_multiple_input[1]  
        virusIndices(p, v)


# In[ ]:





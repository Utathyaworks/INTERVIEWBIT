#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d={}
        f=-1
        for i in range(len(A)-1,-1,-1):
            if A[i] in d:
                f=A[i]
                d[A[i]]+=1
            else:
                d[A[i]]=1
        return f


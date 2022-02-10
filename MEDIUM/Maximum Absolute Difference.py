#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self,A):
        a=[]
        b=[]
        for i in range(len(A)):
            a.append(A[i]+i)
            b.append(A[i]-i)
        return max(max(a)-min(a),max(b)-min(b))


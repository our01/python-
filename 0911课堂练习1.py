#!/usr/bin/env python
# coding: utf-8

# In[14]:


list1=[]
for i in range(0,26):
    list1.append((chr(ord('A')+i),chr(ord('a')+i)))
    print (list1[i][0],'-',list1[i][1])


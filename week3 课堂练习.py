#!/usr/bin/env python
# coding: utf-8

# In[10]:


#练习一 打印九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"X",i,"=",repr(i*j).rjust(2),end="   ")
    print("\n")


# In[ ]:





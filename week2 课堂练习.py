#!/usr/bin/env python
# coding: utf-8

# In[1]:


#练习一

list1=[]
for i in range(0,26):
    list1.append((chr(ord('A')+i),chr(ord('a')+i)))
    print (list1[i][0],'-',list1[i][1])


# In[ ]:


#练习二 1.

import os,sys
base = 'C:/Users/Auder/'
i = 1
for j in range(50):
    file_name = base+"test"+str(i)
    os.mkdir(file_name)
    i=i+1


# In[15]:


#练习二 2.

import os,os.path
dir = "D:\oracle"
 
number_dll = 0
number_exe = 0
number_r0 = 0

for root,dirname,filenames in os.walk(dir):  
       for filename in filenames:  
            if os.path.splitext(filename)[1]=='.dll':
                number_dll += 1

for root,dirname,filenames in os.walk(dir):  
       for filename in filenames:  
            if os.path.splitext(filename)[1]=='.exe':
                number_exe += 1
                
for root,dirname,filenames in os.walk(dir):  
       for filename in filenames:  
            if os.path.splitext(filename)[1]=='.r0':
                number_r0 += 1
print('扩展名为dll的文件数：',number_dll,'\n','扩展名为exe的文件数：',number_exe,'\n','扩展名为r0的文件数：',number_r0)


# In[ ]:





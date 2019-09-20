#!/usr/bin/env python
# coding: utf-8

# In[11]:


a=b=c=d=0
for i in range(0,10000):
    if i%2==0:
        a+=i

for i in range(0,10000):
    if i%3==0:
        b+=i
        
for i in range(0,10000):
    if i%4==0:
        c+=i
        
for i in range(0,10000):
    if i%5==0:
        d+=i
print('10000以内2的倍数的和为：',a)
print('10000以内3的倍数的和为：',b)
print('10000以内4的倍数的和为：',c)
print('10000以内5的倍数的和为：',d)


# In[40]:


asll=[]
j=0
for i in range(32,128):
    asll.append(chr(i))

for i in asll:
    j+=1
    print(i,end="")
    if j==20:
        print('\n')
        j=0


# In[ ]:





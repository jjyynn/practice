#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#l1과 l2가 linked list가 아니라 list 일때 가능한 solution


# In[1]:


def twosum(l1,l2):
    a_list = []
    b_list = []
    return_list = []
        
    for i in l1 :
        a = i * (10 ** int(l1.index(i)))
        a_list.append(a)
        a_sum = sum(a_list)
    for ii in l2 :
        b = ii * (10 ** int(l2.index(ii)))
        b_list.append(b)
        b_sum = sum(b_list)
        
    return_sum = str(a_sum + b_sum)
        
    for s in range(len(str(a_sum + b_sum))):
        return_list.insert(0,int(return_sum[s]))
        
    return return_list


# In[2]:


l1 = [1,0,0,6]
l2 = [4,5,6]
twosum(l1, l2)


# In[3]:


l1 = [0]
l2 = [0]
twosum(l1,l2)


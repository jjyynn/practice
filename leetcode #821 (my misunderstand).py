#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = "loveleetcode"
c = "e"

def short(s,c):
    i = 0
    turn = 1
    c_list = []
    while s.count(c)+1 != turn:
        s_c = s.index(c, i)
        if turn != 1 :
            c_list.append(s_c - sum(c_list))
            i = s_c + 1 
            turn += 1
        else : 
            c_list.append(s_c)
            i = s_c + 1 
            turn += 1

    return c_list
    

short(s,c)


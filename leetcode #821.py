#!/usr/bin/env python
# coding: utf-8

# # ACCEPTED ANSWER

# In[51]:


S = "loveleetcode"
C = 'e'

def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
      lis = data[res[-1]+1:]
    except:
      break     
  return res

def short3(S, C):
    new_list = []
    result_list = []
    c_list = find_index(S, C)
    for i in range(len(S)):   # 0,1,2 ~ 11
        for c in c_list:      # 3,5,6,11
            new_list.append(abs(c-i))
        result_list.append(min(new_list))
        new_list = []
    return result_list


# In[52]:


short3(S,C)


# # PRACTICE

# In[34]:


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


# In[43]:


# Input: S = "loveleetcode", C = 'e'
# Output: 
#  l  o  v  e  l  e  e   t   c   o   d   e
# [3, 2, 1, 0, 1, 0, 0,  1,  2,  2,  1,  0]
#[3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]
# [3, 3, 3, 3, 5, 5, 6, 11, 11, 11, 11, 11]

S = "loveleetcode"
C = 'e'

def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
      lis = data[res[-1]+1:]
    except:
      break     
  return res

###########  1   ##################

# def short1(S, C):
#     new_list = []
#     result_list = []
#     c_list = find_index(S, C)   # [1,2,6]
#     for i in range(len(S)):         # i 가 먼저 for문을 돌때
#         for c in c_list:
#             new_list.append(c - i)
#             result_list.append(min(new_list))
#     return result_list
    

##########  2  ####################

def short2(S, C):
    new_list = []
    result_list = []
    c_list = find_index(S, C)   # [3,5,6,11]
    for c in c_list:               # c가 먼저 for문을 돌때
        for i in range(len(S)):
            new_list.append(c - i)
            result_list.append(min(new_list))
    return result_list

################################

def short3(S, C):
    new_list = []
    result_list = []
    c_list = find_index(S, C)
    for i in range(len(S)):   #0,1,2 ~ 11
        for c in c_list:      # 3,5,6,11
            new_list.append(c-i)
            print(new_list)
#             result_list.append(min(new_list))
            new_list = []
#     return result_list


###### solution ##############

def shortestToChar(self, S, C):
    prev = float('-inf')  #가장 작은 수 
    ans = []
    for i, x in enumerate(S):
        if x == C: prev = i
        ans.append(i - prev)

    prev = float('inf')
    for i in xrange(len(S) - 1, -1, -1):
        if S[i] == C: prev = i
        ans[i] = min(ans[i], prev - i)

    return ans




# find_index(S, C) - 1

# c_list = []
# for i in range(len(S)) :
#     s_c = S.index(C , i)
#     c_list.append(s_c)
    
# c_list


# In[49]:


def short3(S, C):
    new_list = []
    result_list = []
    c_list = find_index(S, C)
    for i in range(len(S)):   # 0,1,2 ~ 11
        for c in c_list:      # 3,5,6,11
            new_list.append(abs(c-i))
        result_list.append(min(new_list))
        new_list = []
    return result_list


# In[50]:


short3(S, C)


# In[22]:


find_index(S, C)


# In[ ]:





# In[ ]:





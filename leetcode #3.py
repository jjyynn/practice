#!/usr/bin/env python
# coding: utf-8

# In[ ]:



### find_index 함수의 코드는 https://pmandocom.tistory.com/17 를 참고하여 가져옴.
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

def lengthOfLongestSubstring(s) : 
    
    
    if bool(s.strip()) == True:
        s_list = []
        i = 0
        last = len(s)
        while i != last:
            s_list.append(s[i]) #s의 각 문자를 하나씩 뜯어 리스트에 저장 = s_list
            i += 1
        
        if len(s) > 2 :   #s의 길이가 3이상이면
            num_list = []
            for i in list(set(s_list)):     #s에 있는 unique를 뽑아 s_list에서 위치 인덱스를 뽑는다 = cal_list
                cal_list = find_index(s_list,i)
                
                if len(cal_list) > 1 :
                    for n in range(len(cal_list)-1): #각 위치 인덱스와 바로 다음 위치 인덱스를 빼고 절댓값을 취해 리스트 저장 = num_list
                        num = abs(cal_list[n] - cal_list[n+1]) #이때 각 cal_list가 하나의 원소만 갖는 길이가 1인 리스트가 있다면 문제가 됨
                        num_list.append(num)
            return max(num_list)
        
        elif len(s) == 2:
            if s_list[0] == s_list[1]: #"aa"
                return 1
            else :                     #"ab"
                return 2
        else :                         #"a"
            return 1
            
    else :
        if s == "":
            return 0
        else:
            return 1


# In[ ]:


#wrong answer because :

s = "aab"
lengthOfLongestSubstring(s)


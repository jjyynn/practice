#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for ii in range(len(nums)):
            if i != ii :
                if target == nums[i] + nums[ii] :
                    result = [i, ii]
                    return result


'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<4:
            return []
        elif nums[0]*4>target or nums[-1]*4<target:
            return []
        elif len(nums)==4 and sum(nums)==target:
            return [nums]
        res=[]
        i=0
        j=i+1
        n=len(nums)
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                k=j+1
                l=n-1
                while k<l:
                    sums=nums[i]+nums[j]+nums[k]+nums[l]
                    if sums==target and [nums[i],nums[j],nums[k],nums[l]] not in res :
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                
                    elif sums<target:
                        k+=1
                    else:
                        l-=1
                j-=1    
                
            i+=1                
        return res
        
        
       
                
        
                

import bisect
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
       
        if k == 0 and t!=0:
            return False
        
        temp=nums[0:k]
        temp.sort()
        
        for i in range(0,len(nums)-1):
            temp.remove(nums[i])
            if k+i<len(nums):
                bisect.insort(temp,nums[k+i]) 
           
            s=0
            l= len(temp)-1
            while s<=l :
                
                mid=int((l+s)/2)
            
                if (nums[i]-t) <=temp[mid]<= (nums[i]+t):
                    return True
                
                if temp[mid] > (nums[i]+t):
                    l=mid-1
            
                elif temp[mid] < (nums[i]-t):
                    s=mid+1
            
                            
        return False

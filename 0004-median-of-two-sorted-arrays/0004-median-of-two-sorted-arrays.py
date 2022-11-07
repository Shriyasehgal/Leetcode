class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l = 0
        r = len(nums1)-1
        total = len(nums1) + len(nums2)
        half = total//2
        while True:
            i = (l+r)//2 #considering the elements in nums1
            j = half - i - 2 #considering the elements in nums2
            left1 = nums1[i] if i>=0 else -float('inf')  
            left2 = nums2[j] if j>=0 else -float('inf')
            right1 = nums1[i+1] if (i+1)<len(nums1) else float('inf')
            right2 = nums2[j+1] if (j+1)<len(nums2) else float('inf')
            #correct partition is found
            if left1<=right2 and left2<=right1:
                if total%2:
                    return min(right1,right2)
                else:
                    return (max(left1,left2) + min(right1,right2))/2
            #We need to add more elemtents from the nums1
            elif left2 > right1:
                l = i+1
            #We need tp remove some elements from the nums2
            else:
                r = i-1
                
            
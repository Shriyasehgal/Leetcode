class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict = {}
        for i in range(len(nums2)):
            num_dict[nums2[i]] = i
        stack = [0]
        nextGreatest = [-1]*len(nums2)
        for i in range(1,len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                nextGreatest[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        for i in range(len(nums1)):
            nums1[i] = nextGreatest[num_dict[nums1[i]]]
        return nums1
        
        
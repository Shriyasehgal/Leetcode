"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""


def threeSum(nums):
    res, d = [], {}
    nums.sort()
    for i in range(len(nums)-2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            t = [nums[i], nums[l], nums[r]]
            if s == 0:
                if str(t) not in d:
                    res.append(t)
                    d[str(t)] = True
                l, r = l + 1, r - 1
            elif s < 0: l += 1
            elif s > 0: r -= 1
    return res
threeSum([-2,0,1,1,2])

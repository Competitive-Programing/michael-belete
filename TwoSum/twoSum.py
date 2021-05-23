class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                sums = nums[i] + nums[j]
                if(sums == target):
                    return [i,j]
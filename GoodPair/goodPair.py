class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if(nums[i] == nums[j] and i < j):
                    goodPairs.append((i, j))
        return len(goodPairs)

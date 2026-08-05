class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in seen:
                return [seen[c],i]
            seen[nums[i]]=i
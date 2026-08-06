class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        for num in nums:
            if num in s:
                duplicate = num
            s.add(num)
        for i in range(1, len(nums) + 1):
            if i not in s:
                return [duplicate, i]
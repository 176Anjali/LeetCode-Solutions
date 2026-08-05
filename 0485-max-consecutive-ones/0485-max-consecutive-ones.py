class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        max_c=0
        for i in nums:
            if i==1:
                c+=1
                if max_c<c:
                    max_c=c
            if i==0:
                c=0
        return max_c
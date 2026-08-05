class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        u=len(nums)-1
        mid=(l+u)//2
        while l<=u:
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                u=mid-1
            else:
                l=mid+1
            mid=(l+u)//2
        else:
            return -1
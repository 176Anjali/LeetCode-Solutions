class Solution(object):
    def countValidSubarrays(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if s% 10 !=x:
                    continue
                t=s
                while t>=10:
                    t//=10
                if t==x:
                    ans+=1
        return ans
class Solution(object):
    def maxTotal(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        n=len(nums)
        NEG=float('-inf')
        dp0=0
        dp1=NEG
        for i in range(n):
            ndp0=NEG
            ndp1=NEG
            if s[i]=='0':
                ndp0=max(dp0,dp1)
                ndp1=NEG
            else:
                ndp1=max(ndp1,dp0+nums[i])
                ndp0=max(ndp0,dp1)
                ndp0=max(ndp0,dp0+nums[i-1] if i>0 else dp0)
                ndp1=max(ndp1,dp1+nums[i])
            dp0,dp1=ndp0,ndp1
        return max(dp0,dp1)    
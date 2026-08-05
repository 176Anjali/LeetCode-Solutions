class Solution(object):
    def maximumMEX(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        res=[]
        i=0
        while i<n:
            mex=0
            while freq.get(mex,0)>0:
                mex+=1
            if mex==0:
                res.extend([0]*(n-i))
                break
            need=set(range(mex))
            j=i
            while j<n:
                x=nums[j]
                if x in need:
                    need.remove(x)
                freq[x]-=1
                if freq[x]==0:
                    del freq[x]
                j+=1
                if not need:
                    break
            res.append(mex)
            i=j
        return res    
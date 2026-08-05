class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        ans=[]
        def dfs(pos,s,cost,prev):
            if cost>k:
                return
            if pos==n:
                ans.append(s)
                return
            dfs(pos+1,s+"0",cost,0)
            if prev==0:
                dfs(pos+1,s+"1",cost+pos,1)
        dfs(0,"",0,0)
        return ans
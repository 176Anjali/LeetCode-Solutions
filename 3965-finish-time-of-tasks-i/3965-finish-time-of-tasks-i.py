class Solution(object):
    def finishTime(self, n, edges, baseTime):
        """
        :type n: int
        :type edges: List[List[int]]
        :type baseTime: List[int]
        :rtype: int
        """
        children=[[] for _ in range(n)]
        for u,v in edges:
            children[u].append(v)
        def dfs(node):
            if not children[node]:
                return baseTime[node]
            mn=float('inf')
            mx=0
            for child in children[node]:
                t=dfs(child)
                mn=min(mn,t)
                mx=max(mx,t)
            ownDuration=(mx-mn)+baseTime[node]
            return mx+ownDuration
        return dfs(0)
                    
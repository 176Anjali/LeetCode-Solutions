class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n=len(items)
        gain=[0]*n
        for i in range(n):
            gain[i]=1
            fi=items[i][0]
            for j in range(n):
                if i !=j and items[j][0] % fi ==0:
                    gain[i]+=1
        dp=[-10**9]*(budget+1)
        dp[0]=0
        for i in range(n):
            price=items[i][1]
            for b in range(budget,price -1, -1):
                dp[b]=max(dp[b],dp[b-price]+gain[i])
        cheapest=min(item[1] for item in items)
        ans=0
        for spent in range(budget+1):
            if dp[spent]<0:
                continue
            remaining=(budget-spent)
            ans=max(ans,dp[spent]+(remaining//cheapest))
        return ans    
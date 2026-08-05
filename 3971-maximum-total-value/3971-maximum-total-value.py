class Solution(object):
    def maxTotalValue(self, value, decay, m):
        """
        :type value: List[int]
        :type decay: List[int]
        :type m: int
        :rtype: int
        """
        MOD=10**9+7
        def count_and_sum(x):
            cnt=0
            total=0
            for v,d in zip(value,decay):
                if v<x:
                    continue
                k=(v-x)//d+1
                if k<=0:
                    continue
                last=v-(k-1)*d
                cnt+=k
                total+=k*(v+last)//2
            return cnt,total
        total_cnt=0
        total_sum=0
        for v,d in zip(value,decay):
            k=(v-1)//d+1
            last=v-(k-1)*d
            total_cnt+=k
            total_sum+=k*(v+last)//2
        if total_cnt<=m:
            return total_sum%MOD
        lo,hi=1,max(value)
        while lo<hi:
            mid=(lo+hi+1)//2
            cnt,_=count_and_sum(mid)
            if cnt>=m:
                lo=mid
            else:
                hi=mid-1
        T=lo
        cnt_above=0
        sum_above=0
        for v,d in zip(value,decay):
            if v<T+1:
                continue
            k=(v-(T+1))//d+1
            if k>0:
                last=v-(k-1)*d
                cnt_above+=k
                sum_above+=k*(v+last)//2
        answer=sum_above+(m-cnt_above)*T
        return answer%MOD
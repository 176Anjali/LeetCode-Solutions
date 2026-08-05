class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
        pq=[(0,0,labels[0],1)]
        dist={}
        while pq:
            d,u,last_char,cnt=heappop(pq)
            state=(u,last_char,cnt)
            if state in dist:
                continue
            dist[state]=d
            if u==n-1:
                return d
            for v,w in graph[u]:
                ch=labels[v]
                if ch==last_char:
                    new_cnt=cnt+1
                else:
                    new_cnt=1
                if new_cnt<=k:
                    new_state=(v,ch,new_cnt)
                    if new_state not in dist:
                        heappush(pq,(d+w,v,ch,new_cnt))
        return -1
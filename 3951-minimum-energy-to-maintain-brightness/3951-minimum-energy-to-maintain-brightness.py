class Solution(object):
    def minEnergy(self, n, brightness, intervals):
        """
        :type n: int
        :type brightness: int
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        total_time=0
        s,e=intervals[0]
        for ns,ne in intervals[1:]:
            if ns<=e+1:
                e=max(e,ne)
            else:
                total_time+=e-s+1
                s,e=ns,ne
        total_time+=e-s+1
        bulbs_needed=(brightness+2)//3
        return bulbs_needed*total_time
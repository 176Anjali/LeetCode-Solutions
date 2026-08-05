class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        u=moves.count('U')
        d=moves.count('D')
        l=moves.count('L')
        r=moves.count('R')
        k=moves.count('_')
        return abs(u-d)+abs(l-r)+k
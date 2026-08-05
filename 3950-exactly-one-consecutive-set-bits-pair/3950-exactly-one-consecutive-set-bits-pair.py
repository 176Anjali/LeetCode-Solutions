class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b=bin(n)[2:]
        count=0
        for i in range(len(b)-1):
            if b[i]=='1'and b[i+1]=='1':
                count+=1
        return count ==1        
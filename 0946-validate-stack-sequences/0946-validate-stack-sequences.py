class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        j=0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return len(stack)==0